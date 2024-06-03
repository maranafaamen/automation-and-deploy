import pandas as pd
import random

import os

SHOPS_NUM = 6
PATH = os.path.join(os.getcwd(), "data")
GOODS = {
    "Kitchen Essentials": [
        {"name": "10-piece cookware set", "price": 89.99},
        {"name": "Stainless steel knife set (6 pieces)", "price": 49.99},
        {"name": "Cutting board (bamboo, large)", "price": 24.99},
        {"name": "Electric kettle (1.7L)", "price": 34.99},
        {"name": "Kitchen scale (digital)", "price": 19.99},
        {"name": "Oven mitts (silicone, set of 2)", "price": 12.99},
    ],
    "Cleaning Supplies": [
        {"name": "All-purpose cleaner (32 oz)", "price": 4.99},
        {"name": "Dish soap (16 oz)", "price": 2.99},
        {"name": "Laundry detergent (64 loads)", "price": 12.99},
        {"name": "Microfiber cleaning cloths (pack of 12)", "price": 9.99},
        {"name": "Mop and bucket set", "price": 24.99},
        {"name": "Vacuum cleaner (bagless)", "price": 99.99},
    ],
    "Bedding and Linens": [
        {"name": "Queen-size bedsheet set (4 pieces)", "price": 49.99},
        {"name": "Duvet cover (queen-size)", "price": 39.99},
        {"name": "Pillow (2-pack, medium-firm)", "price": 24.99},
        {"name": "Bath towel set (6 pieces)", "price": 29.99},
        {"name": "Hand towels (4-pack)", "price": 14.99},
        {"name": "Shower curtain (polyester)", "price": 19.99},
    ],
    "Home Decor": [
        {"name": "Area rug (5'x7')", "price": 79.99},
        {"name": "Throw pillows (set of 2)", "price": 24.99},
        {"name": "Wall clock (12-inch, silent)", "price": 29.99},
        {"name": "Picture frames (set of 3, 8x10 inches)", "price": 19.99},
        {"name": "Scented candles (3-pack, assorted scents)", "price": 14.99},
        {"name": "Artificial plant (medium-sized)", "price": 34.99},
    ],
    "Storage and Organization": [
        {"name": "Storage bins (set of 6, plastic)", "price": 24.99},
        {"name": "Closet organizer (hanging, 6 shelves)", "price": 39.99},
        {"name": "Shoe rack (10-tier, metal)", "price": 29.99},
        {"name": "Laundry hamper (foldable)", "price": 19.99},
        {"name": "Vacuum storage bags (set of 4, large)", "price": 14.99},
        {"name": "Under-bed storage containers (set of 2)", "price": 24.99},
    ],
}

if not os.path.exists(PATH):
    os.makedirs(PATH)


for shop in range(SHOPS_NUM):

    cash_register_num = random.randint(1, 5)

    for cash_register in range(cash_register_num):

        sales = {
            "doc_id": [],
            "item": [],
            "category": [],
            "amount": [],
            "price": [],
            "discount": [],
        }
        sales_num = random.randint(20, 200)

        for doc in range(sales_num):
            items_in_doc = random.randint(1, 10)
            for item in range(items_in_doc):
                rand_category = random.choice(list(GOODS.keys()))
                rand_item = random.choice(GOODS[rand_category])
                position = {
                    "doc_id": f"{shop + 1}_{doc + 1}",
                    "item": rand_item["name"],
                    "category": rand_category,
                    "amount": random.randint(1, 5),
                    "price": rand_item["price"],
                    "discount": random.choice([0, 0, 0, 0, 0, 10, 10, 20, 30, 40, 50]),
                }

                for key, value in position.items():
                    sales[key].append(value)

        sales_df = pd.DataFrame(sales)

        filename = f"{shop + 1}_{cash_register + 1}.csv"

        sales_df.to_csv(os.path.join(PATH, filename), index=False)
