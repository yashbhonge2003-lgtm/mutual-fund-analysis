# To check all columns of csv files

import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        print("\n" + "="*50)
        print(file)
        df = pd.read_csv(os.path.join(folder, file))
        print(df.columns.tolist())