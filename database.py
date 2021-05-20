import psycopg2
import os

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

conn = psycopg2.connect(f"host={db_host} dbname={db_name} user={db_user} password={db_pass}")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE Stock_Prices(
    name text,
    data date,
    open numeric,
    high numeric,
    low numeric,
    close numeric,
    adjclose numeric,
    volume numeric
)
""")
conn.commit()