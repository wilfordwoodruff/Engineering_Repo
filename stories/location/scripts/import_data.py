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
