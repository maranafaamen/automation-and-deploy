import os
import re
import configparser
import csv

from db_connector import PGDatabase

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, 'config.ini'))
PATH = os.path.join(dirname, "data")

DATABASE_CREDS = config['Database']

with PGDatabase(
    host=DATABASE_CREDS['HOST'],
    database=DATABASE_CREDS['DATABASE'],
    user=DATABASE_CREDS['USER'],
    password=DATABASE_CREDS['PASSWORD'],
    ) as database:

    for folder in os.listdir(PATH):
        for file in os.listdir(os.path.join(PATH, folder)):
            if re.match(r'^\d+_\d+\.csv$', file):
                shop_num = re.match(r'^(\d+)_(\d+)\.csv$', file).group(1)
                cash_num = re.match(r'^(\d+)_(\d+)\.csv$', file).group(2)
                with open(os.path.join(PATH, folder, file), 'r') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=',', )
                    next(reader)
                    for row in reader:
                        query = f"""insert into sales values(
                            {folder},
                            {shop_num},
                            {cash_num},
                            {row['doc_id']},
                            '{row['item']}',
                            '{row['category']}',
                            {row['amount']},
                            {row['price']},
                            {row['discount']})"""
                        database.post(query)