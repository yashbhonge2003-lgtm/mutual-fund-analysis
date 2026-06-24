import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "nav_history": "data/processed/02_nav_history_clean.csv",
    "investor_transactions": "data/processed/08_investor_transactions_clean.csv",
    "scheme_performance": "data/processed/07_scheme_performance_clean.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")

print("\nDatabase Created Successfully")