-- 1. TOP 5 FUNDS BY 5Y RETURN
SELECT SCHEME_NAME, RETURN_5YR_PCT
FROM SCHEME_PERFORMANCE
ORDER BY RETURN_5YR_PCT
LIMIT 5;

--2. AVERAGE NAV
SELECT AVG(NAV) AS AVG_NAV
FROM NAV_HISTORY;

--3. MAXIMUM NAV FUND
SELECT amfi_code, MAX(nav) AS max_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY max_nav DESC
LIMIT 5;

--4. TRANSACTIONS BY STATE
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

--5. SIP TRANSACTIONS COUNT
SELECT COUNT(*) AS sip_count
FROM investor_transactions
WHERE transaction_type='SIP';

--6. REDEMPTION TRANSACTIONS COUNT
SELECT COUNT(*) AS redemption_count
FROM investor_transactions
WHERE transaction_type='Redemption';

--7. FUNDS WITH EXPENSE RATIO < 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

--8. AVERAGE RETURN BY CATEGORY
SELECT category,
AVG(return_5yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category;

-- 9. Top Alpha Funds
SELECT scheme_name, alpha
FROM scheme_performance
ORDER BY alpha DESC
LIMIT 10;

-- 10. Risk Grade Distribution
SELECT risk_grade, COUNT(*) AS fund_count
FROM scheme_performance
GROUP BY risk_grade;