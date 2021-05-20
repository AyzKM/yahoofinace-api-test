import requests
import csv
from io import StringIO
import psycopg2
import psycopg2.extras
import os

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

conn = psycopg2.connect(f"host={db_host} dbname={db_name} user={db_user} password={db_pass}")
cur = conn.cursor()
company_name = 'PINS'
url_history_data = 'https://query1.finance.yahoo.com/v7/finance/download/{}?'
params = {
    'range':'2d',
    'interval':'1d',
    'events':'history',
    'includeAdjustedClose':'true'
    }
response = requests.get(url_history_data.format(company_name), params=params)
response.text
file = StringIO(response.text)
reader = csv.reader(file)
all_data = list(reader) 

query = '''
INSERT INTO stock_prices (name, data, open, high, low, close, adjclose, volume)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
'''
values = []
for i in all_data:
    i.insert(0, company_name)
    values.append(tuple(i))
values.pop(0)
psycopg2.extras.execute_batch(cur,query,values)
conn.commit()


