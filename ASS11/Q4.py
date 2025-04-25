
import pandas as pd
data = {
    'John': [True, False, False, True, False, True, False, False, True, False],
    'Judy': [True, False, True, False, False, True, False, True, False, True]
}

df = pd.DataFrame(data)

# A party occurs when both John and Judy are present
df['party'] = df['John'] & df['Judy']

# Compute days until the next party
df['days_til_party'] = df['party'][::-1].cumsum()[::-1] - df['party']

print(df)