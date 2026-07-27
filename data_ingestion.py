import pandas as pd
import os

data_dir = "data/raw"
files = os.listdir(data_dir)

for file in files:
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(data_dir, file))
        print(f"Dataset: {file}")
        print("Shape:", df.shape)
        print("Dtypes:\n", df.dtypes)
        print("Head:\n", df.head(), "\n")
