import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/clean_library.csv")


#10 most listened songs
df_top_songs = df.groupby(["Name", "Artist"])["Play Count"].sum().sort_values(ascending=False).head(10)

#10 most listened artists
df_artist = df.groupby("Artist")["Play Count"].sum().sort_values(ascending=False).head(10)

#10 most listened albums
df_album = df.groupby("Album")["Play Count"].sum().sort_values(ascending=False).head(10)

#10 most skipped songs
df_skips = df.groupby(["Name", "Artist"])["Skip Count"].sum().sort_values(ascending=False).head(10)

#5 Most listened Genres
df_genre = df.groupby("Genre")["Play Count"].sum().sort_values(ascending=False).head(5)

#Total of Genres listened
df_genre_total = df["Genre"].nunique()


#DASHBOARD
fig, axes = plt.subplots(3, 2, figsize=(16, 14))

#10 most listened
df_top_songs.plot(kind="barh", ax=axes[0,0])
axes[0,0].set_title("Top 10 Most Listened Songs")

#10 most listened artists
df_artist.plot(kind="barh", ax=axes[0,1])
axes[0,1].set_title("Top 10 Most Listened Artists")


#10 most listened albums
df_album.plot(kind="barh", ax=axes[1,0])
axes[1,0].set_title("Top 10 Most Listened Albums")



plt.tight_layout(pad=3.0)
plt.show()

