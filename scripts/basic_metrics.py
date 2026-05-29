# scripts/basic_metrics.py

import pandas as pd

df = pd.read_csv("data/postings.csv")

print("Total Jobs:", len(df))
print("Total Companies:", df["company_name"].nunique())
print("Total Locations:", df["location"].nunique())
print("Total Job Titles:", df["title"].nunique())