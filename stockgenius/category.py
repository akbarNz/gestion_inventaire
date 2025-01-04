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
        self.__name = name
        self.__vat = vat

    @property
    def name(self):
        return self.__name

    @property
    def vat(self):
        return self.__vat

    @vat.setter
    def vat(self, new_vat):
        if isinstance(new_vat, float):
            self.vat = new_vat
        else:
            raise TypeError(f"new_vat must be float. {type(new_vat)} not supported")

    def __str__(self):
        return f"Category: {self.name}, VAT: {self.vat}"