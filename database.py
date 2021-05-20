import psycopg2

conn = psycopg2.connect("host=localhost dbname=yf_historical_data user=postgres password=postgres")
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