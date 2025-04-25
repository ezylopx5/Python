import pandas as pd

# a) Date time object for Jan 15 2012
date_a = pd.Timestamp("2012-01-15")

# b) Specific date and time of 9:20 pm
date_b = pd.Timestamp("2012-01-15 21:20:00")

# c) Local date and time
date_c = pd.Timestamp.now()

# d) A date without time
date_d = pd.Timestamp.today().date()

# e) Current date
date_e = pd.Timestamp.today()

# f) Time from a date time
date_f = pd.Timestamp.now().time()

# g) Current local time
date_g = pd.Timestamp.now().time()

print(f"a) {date_a}\nb) {date_b}\nc) {date_c}\nd) {date_d}\ne) {date_e}\nf) {date_f}\ng) {date_g}")