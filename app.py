
# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df.dropna(subset=['title', 'year'])

df = load_data()

# --- Streamlit UI ---
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers dataset")

## Year range slider
#years = sorted(df['year'].dropna().unique())
#year_min, year_max = min(years), max(years)
#year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))

years = sorted(df['year'].dropna().astype(int).unique())  # force int
year_min, year_max = min(years), max(years)

year_range = st.slider(
    "Select year range",
    int(year_min),
    int(year_max),
    (2020, 2021),  # default
    step=1         # make sure step is also int
)


df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.write(df_filtered[['title', 'journal', 'year']].head())

# Publications over time
st.subheader("Publications Over Time")
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Paper Titles")
text = " ".join(df_filtered['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
