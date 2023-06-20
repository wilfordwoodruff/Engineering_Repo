# split locations
import pandas as pd 
import numpy as np
from pull_data import load_data

'''
TODO: make a new dataframe with only unique locations
'''

def transform_data(data): 
    # Filter data to only include journals
    journal_data = data[data["Document Type"] == "Journals"]

    # Exclude NA values from the 'places' column 
    location_data = journal_data[journal_data["Places"].notna()]

    # Get all unique places 
    # Split locations by pipe character and explode into separate rows
    places_data = location_data["Places"].str.split("|").explode().unique()

    # Create final DataFrame 
    final_data = pd.DataFrame({"Location Name": places_data})

     # Add NaN Lat and Long columns 
    final_data["latitude"] = np.nan 
    final_data["longitude"] = np.nan 

    return final_data


