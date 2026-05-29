import pandas as pd

df = pd.read_csv("data/postings.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset Info:")
print(df.info())