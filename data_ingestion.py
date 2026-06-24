# Load all CSV files from raw data folder
# Check dataset structure and data quality
# Display missing values and duplicate records

import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

print(f"Total CSV Files Found: {len(csv_files)}")

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE NAME: {file}")
    print("=" * 60)

    file_path = os.path.join(folder_path, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")