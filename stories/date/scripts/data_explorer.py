import pandas as pd
import re
import os

# Load the data
raw = pd.read_csv("https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv")

# Filter for "Journals" in the Document Type column
all_journals = raw[raw['Document Type'] == "Journals"]


print(raw.head())
print(raw.info())
print(raw['Original Transcript'][0])


data = pd.read_csv('stories/date/data/main_dates_jour.csv')

print(data.head())