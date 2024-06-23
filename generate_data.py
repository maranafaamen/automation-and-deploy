import pandas as pd
import random
import configparser
from datetime import date

import os

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, 'config.ini'))

SHOPS_NUM = int(config['Shops']['SHOPS_NUM'])
PATH = os.path.join(os.path.join(dirname, "data"), str(date.today()))
GOODS = eval(config['Shops']['GOODS'])

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
                    "doc_id": f"{date.today().strftime('%d%m%y')}{shop + 1}{cash_register + 1}{doc + 1}",
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
