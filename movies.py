import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("movies_cleaned.csv")

# Alle einzigartigen Genres extrahieren
all_genres = sorted(set(
    genre
    for genres in df['genres'].dropna()
    for genre in genres.split('|')
))

# Streamlit app title
st.title("🎬 Movie Explorer App")

# Genre selection
selected_genre = st.selectbox("Select a genre:", all_genres)

# Filter movies by selected genre (nur exakter Match)
filtered_movies = df[df['genres'].str.split('|').apply(lambda x: selected_genre in x)]

# Display filtered movies
st.subheader(f"Movies in Genre: {selected_genre}")
st.dataframe(filtered_movies[['Title', 'Year', 'genres']].reset_index(drop=True))

# Bar chart of movie count per genre
st.subheader("Movies per Genre")
genre_counts = df['genres'].str.split('|').explode().value_counts().head(15)
fig, ax = plt.subplots(figsize=(10, 5))
genre_counts.plot(kind='bar', ax=ax, color='steelblue')
ax.set_xlabel("Genre")
ax.set_ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)
