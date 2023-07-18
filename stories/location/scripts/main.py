import pandas as pd
from import_data import get_files
from find_missing import find_missing_data
from split_dataframe import split_dataframe
from replace_nan import replace_nan_with_geolocation
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

# Parse the 'Name' as a list of strings
df['Name'] = df['Name'].str.strip("[]").str.replace("'","").str.split(', ')

# Find the rows where 'latitude' or 'longitude' are missing
missing_values_df, df_no_missing = split_dataframe(df)

# Replace the NaN values with geocoded values
df_filled = replace_nan_with_geolocation(missing_values_df)

# Merge dataframes
df_complete = merge_dataframes(df_no_missing, df_filled)

# Sort dataframe by Name
df_complete.sort_values('Name', inplace=True)

# Save the DataFrame to a new CSV file
df_complete.to_csv('stories/location/data/artifact/new_file3.csv', index=False)
