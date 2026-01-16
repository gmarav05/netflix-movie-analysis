import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Netflix Movies Analysis")

df = pd.read_csv('netflix_titles.csv')

st.subheader("Dataset Preview")
st.dataframe(df.head())

movies = df[df["type"] == "Movie"]
movies_1990s = movies[(movies["release_year"] >= 1990) & (movies["release_year"] < 2000)]

st.subheader("Movie Duration Distribution (1990s)")
fig, ax = plt.subplots()
ax.hist(movies_1990s["duration"])
ax.set_xlabel("Duration (minutes)")
ax.set_ylabel("Number of Movies")
st.pyplot(fig)

tv_shows = df[df['type'] == "TV Show"]
tv_shows['seasons'] = tv_shows['duration'].str.extract(r"(\d+)").astype(int)

short_tv_shows = tv_shows[tv_shows["seasons"] < 2]

st.subheader("TV Shows with less than 2 seasons")
st.write("Count:", short_tv_shows.shape[0])
st.dataframe(short_tv_shows[["title", "duration"]])
