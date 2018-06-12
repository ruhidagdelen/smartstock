import pandas as pd


df = pd.read_csv("csv_files/transactions.csv",parse_dates=[10])

print(df["date"].dtype)

