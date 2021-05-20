from flask import Flask, request
import psycopg2
import json
from psycopg2.extras import RealDictCursor
from main import Encoder
import os

app = Flask(__name__)

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

@app.route('/')
def retriev_data():
    company_name = 'ZUO'
    conn = psycopg2.connect(f"host={db_host} dbname={db_name} user={db_user} password={db_pass}")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query = f"""
    SELECT*FROM stock_prices
    WHERE name = '{company_name}'
    """  
    cur.execute(query)
    if cur.fetchone() is None:
        return ({'message': 'company not found'})
    json_data = json.dumps(cur.fetchall(), cls=Encoder)
    return json_data
