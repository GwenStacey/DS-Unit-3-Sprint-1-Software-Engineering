#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default prouct weight being 20"""
        prod = Product('Some new product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        prod = Product('Some other new product')
        # Stealability should be 0.5 with default values
        self.assertEqual(prod.Stealability(), 0.5)
        # Power should be 10 with default values.
        self.assertEqual(prod.Explode(), 10)


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme tests are working!"""
    def test_default_num_products(self):
        prods = generate_products(30)
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        for prod in generate_products(30):
            first_name, last_name = prod.name.split()
            self.assertIn(first_name, ADJECTIVES)
            self.assertIn(last_name, NOUNS)

if __name__ == '__main__':
    unittest.main()
