import pandas
df = pd.read_excel('SpotifyData.xlsx')
print(df.head())

menuSelect = input("""
Please Select from the following options:
1. View Top Songs for Year
2. Search by Song Name
3. Sort Songs by Traits
4. Filter by BPM
5. Discover Similar Music
6. Search for Artists Top Songs
7. Specialised Insights
""")
print(menuSelect)
