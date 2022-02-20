import sys


class Basket:
    def __init__(self, products, offers):
        self.products = products
        self.offers = offers
        self.items = []
        self.discount = []

    def add_items(self, basket_item):
        # search and find dict for the item present in product catalog
        item_data = next((item for item in self.products if item["name"] == basket_item), None)

        if item_data is None:
            # exits the application since item was not found in the json
            sys.exit("Item not found in product.json")

        # add items dict to the property
        self.items.append(item_data)

        # get offers from json corresponding to the item using id
        # the sell_product_id and buy_product_id are mapped with product's id
        item_discount = next((item for item in self.offers if item["sell_product_id"] == item_data["id"]), None)

        if item_discount and item_discount not in self.discount:
            # add to discount if there is any offer for the product
            self.discount.append(item_discount)

    def calculate(self):
        # finding subtotal of the whole products
        subtotal = sum(item['price'] for item in self.items)
        return subtotal

    def calculate_offer(self):
        item_offers = {}
        for val in self.discount:
            item_count = len([k['id'] for k in self.items if k.get('id') == val['buy_product_id']])
            if item_count < val['buy_product_count']:
                break
            no_of_offers = item_count // val['buy_product_count']
            sell_prod = next((item for item in self.items if item["id"] == val["sell_product_id"]), None)
            item_total_price = no_of_offers * sell_prod['price']
            discounted_amount = item_total_price - (item_total_price * (no_of_offers * val['percentage']) / 100)
            item_offers[val["name"]] = discounted_amount

        return item_offers
