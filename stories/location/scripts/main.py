import pandas as pd
from import_data import get_files
from find_missing import find_missing_data
from split_dataframe import split_dataframe
from replace_nan import replace_nan_with_zero
from merge_dataframes import merge_dataframes

# Load the data
user = "wilfordwoodruff"
repo = "Main-Data"
path = "data/raw"
csv_files = get_files(user, repo, path)

# Sort files by date in the filename, get the latest
csv_files.sort(key=lambda x: x['name'], reverse=True)
latest_file = csv_files[0]

# Construct the raw GitHub URL
raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/main/{latest_file['path']}"

# Read the latest CSV file
df = pd.read_csv(raw_url)

# Extract the 'name', 'latitude', and 'longitude' columns
df = df[['Name', 'Latitude', 'Longitude']]
df['Name'] = df['Name'].str.split('|')
df = df.explode('Name')

# After reading the CSV file and exploding the 'Name' column
print(f"All 'Latitude' values are NaN: {df['Latitude'].isna().all()}")
print(f"All 'Longitude' values are NaN: {df['Longitude'].isna().all()}")


# Find the rows where 'latitude' or 'longitude' are missing
missing_values = find_missing_data(df)

# Separate the dataframe into two; the one with the missing data and the other one with the full dataframe excluding the missing data
missing_values_df, df_no_missing = split_dataframe(df)

# Check if the dataframes are None
print(f'df_no_missing is None: {df_no_missing is None}')
print(f'missing_values_df is None: {missing_values_df is None}')

# Replace the NaN values with 0 values
df_filled = replace_nan_with_zero(missing_values_df)

# Reset the index of the dataframes
df_no_missing.reset_index(drop=True, inplace=True)
df_filled.reset_index(drop=True, inplace=True)

# Merge dataframes
df_complete = merge_dataframes(df_no_missing, df_filled)

# Sort dataframe by Name
df_complete.sort_values('Name', inplace=True)

# Save the DataFrame to a new CSV file
df_complete.to_csv('new_file.csv', index=False)


