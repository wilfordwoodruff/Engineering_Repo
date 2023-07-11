import requests
import json
import re
import pandas as pd

def get_files(user, repo, path):
    url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
    r = requests.get(url)
    data = json.loads(r.text)

    # Filter the files
    csv_files = [file for file in data if re.search(r'\d{4}-\d{2}-\d{2}-places-export\.csv', file['name'])]

    # This will return an array of all the matching files with details
    return csv_files

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

# Now df holds the content of the latest CSV file
print(df.head())