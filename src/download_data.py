
import pandas as pd
import plistlib
import matplotlib.pyplot as plt



with open("data/Library.xml", "rb") as f:
    library = plistlib.load(f)

tracks = library["Tracks"]

df = pd.DataFrame.from_dict(tracks, orient="index")

df = df[df["Apple Music"] == True]
    
df["Total Time"] = (df["Total Time"] / 60000).round(1)
df["Play Count"] = df["Play Count"].fillna(0)
df["Skip Count"] = df["Skip Count"].fillna(0)

keep_cols = ["Name", "Artist", "Album", "Album Artist", "Genre", 
             "Total Time", "Play Count", "Skip Count", "Date Added",
             "Play Date UTC", "Year", "Release Date", "Composer",
             "Sample Rate", "Track Number"]

df = df[keep_cols]

df = df.sort_values("Play Count", ascending=False)
print(df.head(5))

