import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.category import Category


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", 0.2)

    def test_get_name(self):
        self.assertEqual(self.category.name, "Electronics")

    def test_get_vat(self):
        self.assertEqual(self.category.vat, 0.2)

    def test_set_vat(self):
        self.category.vat = 0.18
        self.assertEqual(self.category.vat, 0.18)

    def test_str(self):
        category_str = str(self.category)
        self.assertEqual(category_str, "Category: Electronics, VAT: 0.2")

if __name__ == '__main__':
    unittest.main()