import pandas as pd
import re
import os

# Load the data
# raw = pd.read_csv("https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv")

# # Filter for "Journals" in the Document Type column
# all_journals = raw[raw['Document Type'] == "Journals"]


# print(raw.head())
# print(raw.info())
# print(raw['Original Transcript'][0])


# data = pd.read_csv('stories/date/data/main_dates_jour.csv')

# print(data.head())

# print(raw['Document Type'].unique())

# print(raw[raw['Document Type'] == 'Autobiographies'].info())

df = pd.read_csv('stories\date\data\main_dates_auto.csv')
print(df['date_new'].isna().sum())
print(df.info())
print(df.head())