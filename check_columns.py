import pandas as pd

print("NAV HISTORY")
print(pd.read_csv("data/raw/02_nav_history.csv").columns.tolist())

print("\nINVESTOR TRANSACTIONS")
print(pd.read_csv("data/raw/08_investor_transactions.csv").columns.tolist())

print("\nSCHEME PERFORMANCE")
print(pd.read_csv("data/raw/07_scheme_performance.csv").columns.tolist())