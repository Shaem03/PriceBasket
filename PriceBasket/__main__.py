import argparse
import json

import Basket as Basket

from Basket import Basket


def load_products_offers():
    products_list = []
    offers_list = []

    try:
        # open and add products list from json
        with open(f"{args['product_file']}", "r") as file1:
            for product in json.load(file1):
                products_list.append(product)

        # open and add offers list from json
        with open(f"{args['offers_file']}", "r") as file2:
            for offer in json.load(file2):
                offers_list.append(offer)
    except FileNotFoundError as e:
        print(f"No such file directory: {e.filename}")

    return products_list, offers_list


def main():
    # Load products and offers from json file
    products, offers = load_products_offers()
    # create product basket and add items
    product_basket = Basket(products, offers)
    for val in args["items"]:
        product_basket.add_items(val)

    # print and calculate subtotal of items
    subtotal = product_basket.calculate()
    print('£{:,.2f}'.format(subtotal))

    # get offers for the corresponding items with offer name
    offers = product_basket.calculate_offer()

    # if offers discount is applicable will print the amount of discount
    if offers:
        for key, val in offers.items():
            print(f"{key}:" + "£{:,.2f}".format(val))
    else:
        print("(No offers available)")

    # calculate total discount to be deducted
    discount = sum(list(offers.values()))

    # total after all deduction
    print(f"Total: " + "£{:,.2f}".format(subtotal - discount))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Price Basket of goods')
    parser.add_argument('items', nargs='+', type=str, help='Only items listed in products.json are accepted.')
    parser.add_argument('-p', '--product-file', help='Custom Product file path', required=False,
                        default="product_list.json")
    parser.add_argument('-o', '--offers-file', help='Custom Offers file path', required=False, default="offers.json")
    args = vars(parser.parse_args())
    main()
