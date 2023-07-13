import pandas as pd
import os
import re
from bs4 import BeautifulSoup

# Load the data
raw = pd.read_csv("https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv")

# Filter for "Daybooks" in the Document Type column
all_daybooks = raw[raw['Document Type'] == "Daybooks"]

# Define function to process each row
def process_row(row):
    soup = BeautifulSoup(row['Original Transcript'], 'html.parser')
    date_tags = soup.find_all('date')
    dates = [tag.get('when') for tag in date_tags]
    
    split_pattern = r'(<date when=".+?">|</date>)'
    texts = re.split(split_pattern, row['Original Transcript'])
    texts = [text for text in texts if text.strip()]  # Remove empty strings
    
    # Adjust the length of 'dates' and 'texts' to match each other
    if len(dates) < len(texts):
        dates += [None] * (len(texts) - len(dates))
    elif len(texts) < len(dates):
        texts += [None] * (len(dates) - len(texts))
    
    return pd.DataFrame({
        'Parent_ID': row['Parent ID'],
        'order_id': row['Order'],
        'date': dates,
        'text': texts
    })

# Apply function to each row of the dataframe and concatenate
papers = pd.concat([process_row(row) for _, row in all_daybooks.iterrows()], ignore_index=True)

# Convert date to datetime format and create a new date column in 'mm/dd/yyyy' format
papers['date'] = pd.to_datetime(papers['date'], errors='coerce')
papers['date_new'] = papers['date'].dt.strftime('%m/%d/%Y')

# Get current working directory
current_dir = os.getcwd()

# Build the path to the file
file_path = '../Engineering_Repo/stories/date/data/main_dates_daybooks.csv'

try:
    papers.to_csv(file_path, index=False)
except Exception as e:
    print(f"Could not write file to {file_path}. Error: {e}")
