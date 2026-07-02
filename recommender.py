import pandas as pd

# Load recommendation data
recommendation_df = pd.read_csv("reports/recommendation_data.csv")

# Get user input
risk = input("Enter Risk Appetite (Low / Moderate / High): ").strip().lower()

# Filter funds based on risk category
filtered_df = recommendation_df[
    recommendation_df["risk_category"].str.lower().str.contains(risk, na=False)
]

# Sort by Sharpe Ratio
filtered_df = filtered_df.sort_values(
    by="Sharpe",
    ascending=False
)

# Display top 3 funds
print("\nTop 3 Recommended Funds\n")

if filtered_df.empty:
    print("No funds found for the selected risk category.")
else:
    print(
        filtered_df[
            ["scheme_name", "risk_category", "Sharpe"]
        ].head(3)
    )