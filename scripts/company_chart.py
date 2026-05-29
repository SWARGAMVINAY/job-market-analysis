import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/postings.csv")

top_companies = df["company_name"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_companies.plot(kind="bar")

plt.title("Top 10 Companies by Number of Job Postings")
plt.xlabel("Company")
plt.ylabel("Number of Job Postings")

plt.tight_layout()
plt.show()