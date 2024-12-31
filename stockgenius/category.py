class Category:
    """
    Represents a category of products.

    Attributes:
        name (str): The name of the category.
        vat (float): The VAT rate for the category.
    """

    def __init__(self, name, vat):
        """
        Initializes a new Category instance.

        Args:
            name (str): The name of the category.
            vat (float): The VAT rate for the category.
        """
        self.name = name
        self.vat = vat

    def get_name(self):
        """
        Returns the name of the category.

        Returns:
            str: The name of the category.
        """
        return self.name

    def get_vat(self):
        """
        Returns the VAT rate of the category.

        Returns:
            float: The VAT rate of the category.
        """
        return self.vat

    def set_vat(self, new_vat):
        """
        Updates the VAT rate of the category.

        Args:
            new_vat (float): The new VAT rate of the category.
        """
        self.vat = new_vat