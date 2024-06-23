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
                with open(os.path.join(PATH, folder, file), 'r') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', )
                    next(reader)
                    for row in reader:
                        print(row)
                        query = f"insert into sales values ('{row['dt']}', '{row['company']}', '{row['transaction_type']}', {row['amount']})"
                        database.post(query)