from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from datetime import datetime

# Configure Kivy before importing Window
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

from stockgenius.init_state import init_state
from stockgenius.analytics import SalesAnalytics
from stockgenius.abstract_order import OrderStatus
from stockgenius.order_manager import OrderManager
from stockgenius.purchase_order import PurchaseOrder
# At the top with other imports
from stockgenius.sale_order import SaleOrder
from stockgenius.product import Product

class StockGeniusGUI(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        
        # Initialize inventory
        self.inventory = init_state('stockgenius/data')
        
        # Create tabs
        self.add_dashboard_tab()
        self.add_products_tab()
        self.add_orders_tab()
        self.add_suppliers_tab()

    def add_dashboard_tab(self):
        tab = TabbedPanelItem(text='Dashboard')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add refresh button
        refresh_btn = Button(
            text='Refresh Dashboard',
            size_hint=(1, 0.1)
        )
        refresh_btn.bind(on_press=self.refresh_dashboard)
        
        # Add scrollable dashboard content
        scroll = ScrollView(size_hint=(1, 0.9))
        self.dashboard_content = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None
        )
        self.dashboard_content.bind(minimum_height=self.dashboard_content.setter('height'))
        
        scroll.add_widget(self.dashboard_content)
        layout.add_widget(refresh_btn)
        layout.add_widget(scroll)
        
        tab.add_widget(layout)
        self.add_widget(tab)
        self.refresh_dashboard(None)

    def refresh_dashboard(self, instance):
        self.dashboard_content.clear_widgets()
        analytics = SalesAnalytics(self.inventory)
        dashboard_text = analytics.generate_dashboard()
        
        for line in dashboard_text.split('\n'):
            if line.startswith('='):
                # Section headers
                label = Label(
                    text=line,
                    size_hint_y=None,
                    height=40,
                    bold=True
                )
            else:
                # Regular content
                label = Label(
                    text=line,
                    size_hint_y=None,
                    height=30
                )
            self.dashboard_content.add_widget(label)

    def add_products_tab(self):
        tab = TabbedPanelItem(text='Products')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add product management buttons
        buttons = BoxLayout(size_hint=(1, 0.1), spacing=10)
        buttons.add_widget(Button(text='Add Product'))
        buttons.add_widget(Button(text='Edit Product'))
        buttons.add_widget(Button(text='Remove Product'))
        
        # Add product list
        product_list = ScrollView(size_hint=(1, 0.9))
        products = GridLayout(cols=1, spacing=5, size_hint_y=None)
        products.bind(minimum_height=products.setter('height'))
        
        for product in self.inventory.products:
            products.add_widget(
                Label(
                    text=f"{product.product_id} - {product.name} - Qty: {product.quantity}",
                    size_hint_y=None,
                    height=30
                )
            )
        
        product_list.add_widget(products)
        layout.add_widget(buttons)
        layout.add_widget(product_list)
        tab.add_widget(layout)
        self.add_widget(tab)

    def add_orders_tab(self):
        tab = TabbedPanelItem(text='Orders')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Order type selector
        type_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        sale_btn = ToggleButton(text='Sale Order', group='order_type', state='down')
        purchase_btn = ToggleButton(text='Purchase Order', group='order_type')
        auto_purchase_btn = Button(text='Generate Auto Purchase Orders')
        auto_purchase_btn.bind(on_press=self.generate_auto_purchase_orders)
        
        type_layout.add_widget(sale_btn)
        type_layout.add_widget(purchase_btn)
        type_layout.add_widget(auto_purchase_btn)
        
        # Product selection area
        product_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), spacing=5)
        
        # Product search
        product_search = TextInput(
            multiline=False,
            hint_text='Search product...',
            size_hint=(1, None),
            height=30
        )
        product_search.bind(text=self.filter_products)
        
        # Product dropdown
        self.product_spinner = Spinner(
            text='Select Product',
            values=[f"{p.product_id} - {p.name}" for p in self.inventory.products],
            size_hint=(1, None),
            height=30
        )
        
        # Quantity input
        quantity_input = TextInput(
            multiline=False,
            hint_text='Quantity',
            input_filter='int',
            size_hint=(1, None),
            height=30
        )
        
        # Add product button
        add_product_btn = Button(
            text='Add Product to Order',
            size_hint=(1, None),
            height=30
        )
        add_product_btn.bind(
            on_press=lambda x: self.add_product_to_order(
                self.product_spinner.text,
                quantity_input.text,
                sale_btn.state == 'down'
            )
        )
        
        product_layout.add_widget(product_search)
        product_layout.add_widget(self.product_spinner)
        product_layout.add_widget(quantity_input)
        product_layout.add_widget(add_product_btn)
        
        # Current order display
        order_display = ScrollView(size_hint=(1, 0.4))
        self.current_order_grid = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None
        )
        self.current_order_grid.bind(minimum_height=self.current_order_grid.setter('height'))
        order_display.add_widget(self.current_order_grid)
        
        # Submit order button
        submit_btn = Button(
            text='Submit Order',
            size_hint=(1, 0.1)
        )
        submit_btn.bind(
            on_press=lambda x: self.submit_order(sale_btn.state == 'down')
        )
        
        # Order list
        order_list = ScrollView(size_hint=(1, 0.4))
        self.orders_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.orders_grid.bind(minimum_height=self.orders_grid.setter('height'))
        self.refresh_order_list()
        order_list.add_widget(self.orders_grid)
        
        # Add all components
        layout.add_widget(type_layout)
        layout.add_widget(product_layout)
        layout.add_widget(order_display)
        layout.add_widget(submit_btn)
        layout.add_widget(order_list)
        
        tab.add_widget(layout)
        self.add_widget(tab)

    def filter_products(self, instance, value):
        """Filter products based on search input."""
        filtered = [
            f"{p.product_id} - {p.name}" 
            for p in self.inventory.products 
            if value.lower() in p.name.lower() or value in p.product_id
        ]
        self.product_spinner.values = filtered if filtered else ['No products found']

    def add_product_to_order(self, product_text, quantity, is_sale):
        """Add a product to the current order."""
        if not product_text or product_text == 'Select Product' or not quantity:
            return
        
        product_id = product_text.split(' - ')[0]
        product = self.inventory.get_product_by_id(product_id)
        if not product:
            return
        
        try:
            qty = int(quantity)
            if qty <= 0 or (is_sale and qty > product.quantity):
                return
                
            # Add to current order display
            self.current_order_grid.add_widget(
                Label(
                    text=f"{product.name} x {qty} = ${product.price * qty:.2f}",
                    size_hint_y=None,
                    height=30
                )
            )
        except ValueError:
            return

    def submit_order(self, is_sale):
        """Submit the current order."""
        if not self.current_order_grid.children:
            return
            
        order_id = f"{'SO' if is_sale else 'PO'}{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
        # Collect products from current order grid
        products = []
        for widget in self.current_order_grid.children:
            # Parse product info from label text
            # Format: "ProductName x Quantity = $Total"
            product_info = widget.text.split(' x ')
            product_name = product_info[0]
            quantity = int(product_info[1].split(' = ')[0])
            
            # Find product in inventory
            product = next(
                (p for p in self.inventory.products if p.name == product_name),
                None
            )
            
            if product:
                # Create a copy of the product with ordered quantity
                order_product = Product(
                    product.product_id,
                    product.name,
                    quantity,
                    product.price,
                    product.category,
                    product.supplier
                )
                products.append(order_product)
        
        if products:
            if is_sale:
                # Create and add sale order
                order = SaleOrder(order_id, products)
                self.inventory.add_sale_order(order)
            else:
                # Get supplier from first product (assuming all products from same supplier)
                supplier = products[0].supplier
                order = PurchaseOrder(order_id, products, supplier)
                self.inventory.add_purchase_order(order)
            
            # Clear current order display
            self.current_order_grid.clear_widgets()
            # Refresh order list
            self.refresh_order_list()

    def refresh_order_list(self):
        """Refresh the list of orders."""
        self.orders_grid.clear_widgets()
        
        # Add sale orders
        for order in self.inventory.sale_orders:
            order_layout = BoxLayout(size_hint_y=None, height=40)
            order_layout.add_widget(Label(text=str(order)))
            status_spinner = Spinner(
                text=order.status.value,
                values=[s.value for s in OrderStatus],
                size_hint_x=0.3
            )
            status_spinner.bind(
                text=lambda x, v, o=order: self.update_order_status(o, v)
            )
            order_layout.add_widget(status_spinner)
            self.orders_grid.add_widget(order_layout)
        
        # Add purchase orders
        for order in self.inventory.purchase_orders:
            order_layout = BoxLayout(size_hint_y=None, height=40)
            order_layout.add_widget(Label(text=str(order)))
            status_spinner = Spinner(
                text=order.status.value,
                values=[s.value for s in OrderStatus],
                size_hint_x=0.3
            )
            status_spinner.bind(
                text=lambda x, v, o=order: self.update_order_status(o, v)
            )
            order_layout.add_widget(status_spinner)
            self.orders_grid.add_widget(order_layout)

    def update_order_status(self, order, new_status):
        """Update an order's status."""
        try:
            status = OrderStatus(new_status)
            old_status = order.status
            order.status = status
            
            # Update quantities if delivered
            if status == OrderStatus.DELIVERED and old_status != OrderStatus.DELIVERED:
                for product in order.products:
                    original_product = self.inventory.get_product_by_id(product.product_id)
                    if original_product:
                        if isinstance(order, PurchaseOrder):
                            original_product.quantity += product.quantity
                        else:
                            original_product.quantity -= product.quantity
        except ValueError:
            pass

    def generate_auto_purchase_orders(self, instance):
        """Generate automated purchase orders for low stock items."""
        order_manager = OrderManager(self.inventory)
        order_manager.check_stock_levels()
        self.refresh_order_list()

    def add_suppliers_tab(self):
        """Add the suppliers management tab."""
        tab = TabbedPanelItem(text='Suppliers')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add supplier management buttons
        buttons = BoxLayout(size_hint=(1, 0.1), spacing=10)
        buttons.add_widget(Button(text='Add Supplier'))
        buttons.add_widget(Button(text='Edit Supplier'))
        buttons.add_widget(Button(text='Remove Supplier'))
        
        # Add supplier list
        supplier_list = ScrollView(size_hint=(1, 0.9))
        suppliers = GridLayout(cols=1, spacing=5, size_hint_y=None)
        suppliers.bind(minimum_height=suppliers.setter('height'))
        
        for supplier in self.inventory.suppliers:
            supplier_info = BoxLayout(size_hint_y=None, height=30)
            supplier_info.add_widget(
                Label(
                    text=f"{supplier.supplier_id} - {supplier.name}",
                    size_hint_x=0.7
                )
            )
            supplier_info.add_widget(
                Label(
                    text=f"Products: {len(supplier.products)}",
                    size_hint_x=0.3
                )
            )
            suppliers.add_widget(supplier_info)
        
        supplier_list.add_widget(suppliers)
        layout.add_widget(buttons)
        layout.add_widget(supplier_list)
        tab.add_widget(layout)
        self.add_widget(tab)

class StockGeniusApp(App):
    def build(self):
        return StockGeniusGUI()

if __name__ == '__main__':
    try:
        StockGeniusApp().run()
    except Exception as e:
        print(f"Error starting application: {e}")