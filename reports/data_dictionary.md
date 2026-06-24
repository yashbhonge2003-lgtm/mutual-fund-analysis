# Mutual Fund Analytics Data Dictionary

## 01_fund_master.csv

| Column | Description |
|----------|-------------|
| amfi_code | Unique AMFI Scheme Code |
| scheme_name | Name of Mutual Fund Scheme |
| fund_house | AMC Name |
| category | Fund Category |

---

## 02_nav_history.csv

| Column | Description |
|----------|-------------|
| amfi_code | Fund Identifier |
| date | NAV Date |
| nav | Net Asset Value |

---

## 07_scheme_performance.csv

| Column | Description |
|----------|-------------|
| return_1yr_pct | 1 Year Return |
| return_3yr_pct | 3 Year Return |
| return_5yr_pct | 5 Year Return |
| expense_ratio_pct | Expense Ratio |
| alpha | Alpha |
| beta | Beta |
| sharpe_ratio | Sharpe Ratio |
| risk_grade | Risk Category |

---

## 08_investor_transactions.csv

| Column | Description |
|----------|-------------|
| investor_id | Investor Identifier |
| transaction_date | Transaction Date |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction Amount |
| state | Investor State |
| city | Investor City |
| kyc_status | KYC Verification Status |