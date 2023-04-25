
import pandas as pd
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Louis Pulford\\Desktop\\SpotifyDataBackup.csv', encoding='iso-8859-1')

year = 2020
year2 = 2021
df_filtered = df[df['year'] == year].nlargest(100,'popularity')
df_filtered2 = df[df['year'] == year2].nlargest(100,'popularity')

bar_width = 0.4

plt.plot(df_filtered['popularity'], df_filtered['tempo'], marker='o', linestyle='--', color='red')
plt.title('popularity compared to tempo')
plt.xlabel('popularity')
plt.ylabel('tempo')
plt.grid(True)
plt.show()


# Get the average energy and danceability for each year
df_avg = df.groupby('year').mean()[['energy', 'danceability']]
df_avg_filtered = df_avg.loc[[year]]

# Plot the bar chart
bar_width = 0.4
plt.bar(df_avg_filtered.index, df_avg_filtered['energy'], width=bar_width, color='green', label='Energy')
plt.bar(df_avg_filtered.index + bar_width, df_avg_filtered['danceability'], width=bar_width, color='blue', label='Danceability')

plt.title(f'Average energy and danceability for year {year}')
plt.xlabel('Year')
plt.ylabel('Value')
plt.ylim([0, 1])
plt.legend()
plt.show()


plt.plot(df_filtered['popularity'], df_filtered['energy'], marker='o', linestyle='--', color='red')
plt.title('popularity compared to energy')
plt.xlabel('popularity')
plt.ylabel('energy')
plt.grid(True)
plt.show()

plt.plot(df_filtered['popularity'], df_filtered['valence'], marker='o', linestyle='--', color='red')
plt.title('popularity compared to valence')
plt.xlabel('popularity')
plt.ylabel('valence')
plt.grid(True)
plt.show()