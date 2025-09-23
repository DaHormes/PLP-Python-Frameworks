
# part3_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df_clean = df.dropna(subset=['title', 'year'])

# --- Publications by year ---
year_counts = df_clean['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# --- Top journals ---
top_journals = df_clean['journal'].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.show()

# --- Word cloud of titles ---
text = " ".join(df_clean['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Frequent Words in Titles")
plt.show()

# --- Source distribution ---
df_clean['source_x'].value_counts().head(10).plot(kind='bar')
plt.title("Paper Counts by Source")
plt.ylabel("Count")
plt.show()

