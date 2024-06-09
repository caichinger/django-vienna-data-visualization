import pandas as pd


PRECIPITATION = 'precipitation totals'
RAIN = PRECIPITATION
SUNSHINE = 'hours of sunshine'
SUN = SUNSHINE
MONTH = 'month'
YEAR_MONTH = 'year_month'
SEASON = 'season'
MONTH_TO_SEASON = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}

data = pd.read_parquet('./data/all.parquet')
data[MONTH] = data[YEAR_MONTH].dt.month
data[SEASON] = data[MONTH].replace(MONTH_TO_SEASON)
data.head()
