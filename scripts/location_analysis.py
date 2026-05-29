import pandas as pd

df = pd.read_csv("data/postings.csv")

print(df["location"].value_counts().head(50))