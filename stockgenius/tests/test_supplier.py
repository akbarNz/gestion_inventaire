import unittest
from stockgenius.supplier import Supplier
from stockgenius.product import Product
from stockgenius.category import Category

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001", 
            "Tech Supplies Inc", 
            "John Doe", 
            "john@techsupplies.com", 
            "123-456-7890", 
            "123 Tech Street"
        )
        self.category = Category("Electronics", 0.2)
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category, self.supplier)

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.supplier_id, "S001")
        self.assertEqual(self.supplier.name, "Tech Supplies Inc")
        self.assertEqual(self.supplier.contact_person, "John Doe")
        self.assertEqual(self.supplier.email, "john@techsupplies.com")
        self.assertEqual(self.supplier.phone, "123-456-7890")
        self.assertEqual(self.supplier.address, "123 Tech Street")
        self.assertTrue(self.supplier.active)

    def test_add_product(self):
        self.supplier.add_product(self.product)
        self.assertIn(self.product, self.supplier.products)

    def test_remove_product(self):
        self.supplier.add_product(self.product)
        self.supplier.remove_product("P001")
        self.assertNotIn(self.product, self.supplier.products)

    def test_update_contact_info(self):
        self.supplier.update_contact_info(
            email="newemail@techsupplies.com",
            phone="987-654-3210",
            contact_person="Jane Doe"
        )
        self.assertEqual(self.supplier.email, "newemail@techsupplies.com")
        self.assertEqual(self.supplier.phone, "987-654-3210")
        self.assertEqual(self.supplier.contact_person, "Jane Doe")

    def test_str(self):
        expected = "Supplier(S001, Tech Supplies Inc, Active: True)"
        self.assertEqual(str(self.supplier), expected)

if __name__ == '__main__':
    unittest.main()