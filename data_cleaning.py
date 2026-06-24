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

# ==========================
# FUND MASTER
# ==========================

fund = pd.read_csv("data/raw/01_fund_master.csv")

fund = fund.drop_duplicates()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

for col in [
    "expense_ratio_pct",
    "exit_load_pct",
    "min_sip_amount",
    "min_lumpsum_amount"
]:
    fund[col] = pd.to_numeric(
        fund[col],
        errors="coerce"
    )

fund.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)

print("Fund Master Cleaned")


# ==========================
# AUM BY FUND HOUSE
# ==========================

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

for col in [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]:
    aum[col] = pd.to_numeric(
        aum[col],
        errors="coerce"
    )

aum = aum[aum["aum_crore"] >= 0]

aum = aum.drop_duplicates()

aum.to_csv(
    "data/processed/03_aum_by_fund_house_clean.csv",
    index=False
)

print("AUM Data Cleaned")


# ==========================
# MONTHLY SIP INFLOWS
# ==========================

sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

for col in [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]:
    sip[col] = pd.to_numeric(
        sip[col],
        errors="coerce"
    )

sip = sip.drop_duplicates()

sip.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)

print("Monthly SIP Cleaned")


# ==========================
# CATEGORY INFLOWS
# ==========================

cat = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

cat["net_inflow_crore"] = pd.to_numeric(
    cat["net_inflow_crore"],
    errors="coerce"
)

cat = cat.drop_duplicates()

cat.to_csv(
    "data/processed/05_category_inflows_clean.csv",
    index=False
)

print("Category Inflows Cleaned")


# ==========================
# INDUSTRY FOLIO COUNT
# ==========================

folio = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

for col in [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]:
    folio[col] = pd.to_numeric(
        folio[col],
        errors="coerce"
    )

folio = folio.drop_duplicates()

folio.to_csv(
    "data/processed/06_industry_folio_count_clean.csv",
    index=False
)

print("Industry Folio Count Cleaned")


# ==========================
# PORTFOLIO HOLDINGS
# ==========================

hold = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

hold["portfolio_date"] = pd.to_datetime(
    hold["portfolio_date"],
    errors="coerce"
)

for col in [
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]:
    hold[col] = pd.to_numeric(
        hold[col],
        errors="coerce"
    )

hold = hold[
    (hold["weight_pct"] >= 0)
    & (hold["weight_pct"] <= 100)
]

hold = hold.drop_duplicates()

hold.to_csv(
    "data/processed/09_portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio Holdings Cleaned")


# ==========================
# BENCHMARK INDICES
# ==========================

bench = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

bench["date"] = pd.to_datetime(
    bench["date"],
    errors="coerce"
)

bench["close_value"] = pd.to_numeric(
    bench["close_value"],
    errors="coerce"
)

bench = bench.drop_duplicates()

bench.to_csv(
    "data/processed/10_benchmark_indices_clean.csv",
    index=False
)

print("Benchmark Indices Cleaned")

print("\nAll 10 CSV Files Cleaned Successfully")