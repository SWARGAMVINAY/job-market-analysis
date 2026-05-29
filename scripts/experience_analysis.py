 

import pandas as pd

df = pd.read_csv("data/postings.csv")

print(
    df["formatted_experience_level"]
    .value_counts(dropna=False)
    .head(20)
)