import pandas as pd
import numpy as np
from get_location import get_location_by_name

def replace_nan_with_geolocation(df):
    new_df = df.copy()
    for i, row in new_df.iterrows():
        if pd.isna(row['Latitude']) or pd.isna(row['Longitude']):
            lat, lon = get_location_by_name(row['Name'])
            if lat and lon:
                new_df.at[i, 'Latitude'] = lat
                new_df.at[i, 'Longitude'] = lon
    return new_df

