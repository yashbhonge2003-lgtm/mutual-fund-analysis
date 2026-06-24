import pandas as pd

# ==========================
# NAV HISTORY CLEANING
# ==========================

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"], errors="coerce")

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

nav_df["nav"] = (
    nav_df.groupby("amfi_code")["nav"]
    .ffill()
)

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df["nav"] > 0]

nav_df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")


# ==========================
# INVESTOR TRANSACTIONS
# ==========================

txn_df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"],
    errors="coerce"
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .replace({
        "SIP": "SIP",
        "LUMPSUM": "Lumpsum",
        "REDEMPTION": "Redemption"
    })
)

txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn_df["kyc_valid"] = (
    txn_df["kyc_status"]
    .isin(valid_kyc)
)

txn_df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")


# ==========================
# SCHEME PERFORMANCE
# ==========================

perf_df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

perf_df["expense_ratio_flag"] = ~(
    perf_df["expense_ratio_pct"]
    .between(0.1, 2.5)
)

perf_df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned")
print("All Cleaning Completed Successfully")