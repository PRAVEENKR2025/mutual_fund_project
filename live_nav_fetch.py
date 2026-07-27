import requests
import pandas as pd

# Fetch HDFC Top 100 NAV
url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data['data'])
df.to_csv("data/raw/hdfc_top100_nav.csv", index=False)

# Fetch NAV for 5 key schemes
scheme_codes = {
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

for name, code in scheme_codes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['data'])
    df.to_csv(f"data/raw/{name.replace(' ', '_').lower()}_nav.csv", index=False)

print("✅ NAV data fetched and saved in data/raw")
