import pandas as pd

df = pd.read_csv("data/postings.csv")

top_companies = df["company_name"].value_counts().head(20)

print(top_companies)