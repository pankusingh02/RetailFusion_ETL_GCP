from extract.extract_api import extract_exchange_rates


df = extract_exchange_rates("EUR", ["USD", "INR"])

print(df)