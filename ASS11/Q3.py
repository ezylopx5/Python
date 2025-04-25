import pandas as pd 

# Sample data
asking_prices = pd.Series([12000, 15000, 18000, 20000, 17000])
fair_prices = pd.Series([12500, 14000, 18500, 19000, 17500])

# Finding good deals (where asking price is less than fair price)
good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print("Good deal indices:", good_deals)