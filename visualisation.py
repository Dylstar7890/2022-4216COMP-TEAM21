import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\paddy\\Downloads\\data.csv')

new_df = df[df["year"] > 2019]

# This graph shows the relationship between danceability and popularity of a song.

plt.title("Danceability compared to popularity (2020 only)")
plt.plot(new_df.danceability, new_df.popularity, "ro", markersize=2)

plt.xlabel("Danceability")
plt.ylabel("Popularity")

plt.show()

# This graph shows the valence of 20,000 songs as a histogram.

plt.hist(df.valence)

plt.xlabel("Valence")
plt.ylabel("Number of songs")

plt.title("Valence in songs")

plt.show()
