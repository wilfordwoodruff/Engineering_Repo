import pandas as pd
import os
import re
from bs4 import BeautifulSoup

# Load the data
raw = pd.read_csv("https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv")

# Filter for "Autobiographies" in the Document Type column
all_autobiographies = raw[raw['Document Type'] == "Autobiographies"]

# Define function to process each row
def process_row(row):
    soup = BeautifulSoup(row['Original Transcript'], 'html.parser')
    
    # Assuming the date is in the format YYYY-MM-DD
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', row['Original Transcript'])
    
    split_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    texts = re.split(split_pattern, row['Original Transcript'])
    
    # If the length of 'dates' is less than 'texts', add None to 'dates'
    dates += [None] * (len(texts) - len(dates))
    
    return pd.DataFrame({
        'Parent_ID': row['Parent ID'],
        'order_id': row['Order'],
        'date': dates,
        'text': texts
    })

# Apply function to each row of the dataframe and concatenate
papers = pd.concat([process_row(row) for _, row in all_autobiographies.iterrows()], ignore_index=True)

# Convert date to datetime format and create a new date column in 'mm/dd/yyyy' format
papers['date'] = pd.to_datetime(papers['date'], errors='coerce')
papers['date_new'] = papers['date'].dt.strftime('%m/%d/%Y')

# Get current working directory
current_dir = os.getcwd()

# Build the path to the file
file_path = '../Engineering_Repo/stories/date/data/main_dates_auto.csv'


try:
    papers.to_csv(file_path, index=False)
except Exception as e:
    print(f"Could not write file to {file_path}. Error: {e}")
