import pandas as pd

# Load the data
df1 = pd.read_csv('stories\date\data\main_dates_jour.csv')
df2 = pd.read_csv('stories\stories\date\data\main_dates_jour.csv')

# Convert the 'date' columns to datetime format
df1['date'] = pd.to_datetime(df1['date'], errors='coerce')
df2['date'] = pd.to_datetime(df2['date'], errors='coerce')

# Print the number of NaT rows in each DataFrame
print('Number of skipped rows in df1:', df1['date'].isna().sum())
print('Number of skipped rows in df2:', df2['date'].isna().sum())

# Find rows where the dates are the same
same_dates = df1[df1['date'].isin(df2['date'])]

print(same_dates)
