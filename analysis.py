import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the cleaned dataset
nav_data = pd.read_csv("data/processed/cleaned_nav.csv")

# Step 2: Convert date column to datetime (safety check)
nav_data['date'] = pd.to_datetime(nav_data['date'])

# Step 3: Plot NAV trends for each fund
plt.figure(figsize=(12,6))
for fund in nav_data['fund_name'].unique():
    subset = nav_data[nav_data['fund_name'] == fund]
    plt.plot(subset['date'], subset['nav'], label=fund)

plt.legend()
plt.title("NAV Trends Over Time")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.grid(True)
plt.tight_layout()
plt.savefig("reports/nav_trends.png")
plt.show()

# Step 4: Calculate returns (percentage change)
nav_data['returns'] = nav_data.groupby('fund_name')['nav'].pct_change()

# Step 5: Save dataset with returns
nav_data.to_csv("data/processed/nav_with_returns.csv", index=False)

print("✅ Analysis complete: plots saved in reports/, returns added to dataset")
