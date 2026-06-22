import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

# print("Columns in Dataset:")
# print(df.columns)

# print("\nFirst 5 Rows:")
# print(df.head())

# print(df.columns.tolist())


print("\nUNIQUE FUND HOUSES")
print(df["fund_house"].unique())

print("\nUNIQUE CATEGORIES")
print(df["category"].unique())

print("\nUNIQUE SUB-CATEGORIES")
print(df["sub_category"].unique())

print("\nUNIQUE RISK CATEGORIES")
print(df["risk_category"].unique())