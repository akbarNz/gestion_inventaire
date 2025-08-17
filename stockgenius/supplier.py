class Supplier:
    """
    Represents a supplier in the inventory system.

    Attributes:
        supplier_id (str): Unique identifier for the supplier
        name (str): Company name of the supplier
        contact_person (str): Name of primary contact
        email (str): Contact email
        phone (str): Contact phone number
        address (str): Business address
        products (list): List of products supplied by this supplier
        active (bool): Whether the supplier is currently active
    """

    def __init__(self, supplier_id, name, contact_person, email, phone, address):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_person = contact_person
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__products = []
        self.__active = True

    @property
    def supplier_id(self):
        return self.__supplier_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def contact_person(self):
        return self.__contact_person

    @contact_person.setter
    def contact_person(self, new_contact):
        self.__contact_person = new_contact

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def products(self):
        return self.__products

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, status):
        self.__active = status

    def add_product(self, product):
        """Add a product to supplier's catalog."""
        if product not in self.__products:
            self.__products.append(product)

    def remove_product(self, product_id):
        """Remove a product from supplier's catalog."""
        self.__products = [p for p in self.__products if p.product_id != product_id]

    def update_contact_info(self, email=None, phone=None, contact_person=None):
        """Update supplier contact information."""
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if contact_person:
            self.contact_person = contact_person

    def __str__(self):
        return f"Supplier({self.supplier_id}, {self.name}, Active: {self.active})"