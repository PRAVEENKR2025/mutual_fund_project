import pandas as pd
import glob

# Load all NAV CSVs from data/raw
files = glob.glob("data/raw/*_nav.csv")

dfs = []
for file in files:
    df = pd.read_csv(file)
    # Add fund name from filename
    df['fund_name'] = file.split("\\")[-1].replace("_nav.csv", "")
    dfs.append(df)

# Combine into one DataFrame
nav_data = pd.concat(dfs, ignore_index=True)

# Clean columns
nav_data['date'] = pd.to_datetime(nav_data['date'], dayfirst=True)
nav_data['nav'] = pd.to_numeric(nav_data['nav'], errors='coerce')

# Drop missing values
nav_data = nav_data.dropna()

# Save cleaned dataset
nav_data.to_csv("data/processed/cleaned_nav.csv", index=False)

print("✅ Cleaned NAV data saved in data/processed")
