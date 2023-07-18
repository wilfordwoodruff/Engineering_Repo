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
# df_complete.to_csv('stories/location/data/artifact/new_file.csv', index=False)

# Counting how many sad faces are there after finding the location coordinates that match both the csv files
sad_face_count = df_complete[(df_complete['Latitude'] == ":(") | (df_complete['Longitude'] == ":(")].shape[0]

print(f"There are {sad_face_count} rows where 'Latitude' or 'Longitude' are ':('")
# answer: There are 2188 rows where 'Latitude' or 'Longitude' are ':('

# Now df_sad_face is a DataFrame containing only the rows where either 'Latitude' or 'Longitude' are ':('
df_sad_face = df_complete[(df_complete['Latitude'] == ":(") | (df_complete['Longitude'] == ":(")]

# Create a new CSV file 'missing_locations.csv' that contains only the rows with missing Latitude or Longitude values
df_sad_face.to_csv('stories/location/data/artifact/missing_locations.csv', index=False)

# Now df_no_sad_face is a DataFrame containing only the rows where neither 'Latitude' nor 'Longitude' are ':('
df_no_sad_face = df_complete[(df_complete['Latitude'] != ":(") & (df_complete['Longitude'] != ":(")]

# Create a new CSV file 'complete_locations.csv' that contains only the rows without missing Latitude or Longitude values
df_no_sad_face.to_csv('stories/location/data/artifact/complete_locations.csv', index=False)

