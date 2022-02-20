import unittest

from PriceBasket import Basket


class Test(unittest.TestCase):
    products = [{
        "id": 1,
        "name": "Rice",
        "price": 10.00,
        "unit_type": "bag"
    },
        {
            "id": 2,
            "name": "onion",
            "price": 19.99,
            "unit_type": "bag"
        }]
    offers = [{
        "id": 1,
        "name": "Buy 2 bag onion and get 30 off on rice",
        "buy_product_id": 2,
        "sell_product_id": 1,
        "buy_product_count": 2,
        "percentage": 30
    }]
    basket = Basket.Basket(products, offers)

    def test_add_items(self):
        item1 = "Rice"
        self.basket.add_items(item1)
        self.assertEqual(self.products, self.products)

    def test_invalid_item(self):
        item2 = "milk"
        with self.assertRaises(SystemExit) as cm:
            self.basket.add_items(item2)

        self.assertEqual(cm.exception.code, "Item not found in product.json")

    def test_calculate(self):
        item = "onion"
        self.basket.add_items(item)
        self.assertEqual(self.basket.calculate(), 29.99)

    def test_offer(self):
        item = "onion"
        self.basket.add_items(item)
        discount = 10 - 10 * (30 / 100)
        self.assertEqual(list(self.basket.calculate_offer().values())[0], discount)
