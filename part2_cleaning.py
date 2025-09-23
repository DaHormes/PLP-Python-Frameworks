
# part2_cleaning.py
import pandas as pd

df = pd.read_csv("metadata.csv")

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Create word count column for abstracts
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Drop rows where title or year is missing (for clarity)
df_clean = df.dropna(subset=['title', 'year'])

print(df_clean[['title', 'year', 'abstract_word_count']].head())
