from extract.extract_sql import extract_orders_from_postgres

df = extract_orders_from_postgres()
print(df)
