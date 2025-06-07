from extract.extract_csv import extract_csv  # Import our extraction function

csv_path='sample_data.csv'

df= extract_csv(csv_path)

print(df.head())