# PriceBasket

Execute as follows to show usage:

```
python PriceBasket -h
usage: PriceBasket [-h] [-p PRODUCT_FILE] [-o OFFERS_FILE] items [items ...]

Price Basket of goods

positional arguments:
  items                 Only items listed in products.json are accepted.

optional arguments:
  -h, --help            show this help message and exit
  -p PRODUCT_FILE, --product-file PRODUCT_FILE
                        Custom Product file path
  -o OFFERS_FILE, --offers-file OFFERS_FILE
                        Custom Offers file path
 
```

## Run Application

Examples:

``` 
python PriceBasket Apples Milk Bread 

output:
£3.10
Apples 10% off this week: -£0.90
Total: £2.20

python PriceBasket Apples Milk Bread Apples Soup Soup

output:
£5.40
Apples 10% off this week: -£1.60
Buy 2 tins of soup and get a loaf of bread at 50% off: -£0.40
Total: £3.40

python PriceBasket Milk Bread Soup

output:
£2.75
(No offers available)
Total: £2.75

```

### Custom products and offers can be added via cli

```
python PriceBasket Apples Milk Bread -p cutom-product.json

python PriceBasket Apples Milk Bread -o cutom-offers.json
```

### The Product input sample

```json
{
  "id": 1,
  "name": "Milk",
  "price": 1.3,
  "unit_type": "bottle"
}
```

### The Offer input sample

```
{
  "id": 1,
  "name": "Apples 10% off this week", // offer title
  "buy_product_id": 4, // product id of the iem to be purchased
  "sell_product_id": 4, // product id of item which will get discount
  "buy_product_count": 1, // count of product to get the offer
  "percentage": 10 // percentage of the offer
}
```