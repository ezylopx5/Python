# Sample dataset
import pandas as pd

concerts = pd.DataFrame({
    'artist': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'A', 'B'],
    'venue': ['X', 'Y', 'X', 'Z', 'Y', 'Z', 'X', 'Z', 'X', 'Y'],
    'date': pd.date_range(start="2023-01-01", periods=10, freq='M')
})

# Extract year-month from date
concerts['year_month'] = concerts['date'].dt.to_period('M')

# Group by (artist, venue) and count concerts
concert_counts = concerts.groupby(['year_month', 'artist', 'venue']).size().unstack(fill_value=0)

print(concert_counts)