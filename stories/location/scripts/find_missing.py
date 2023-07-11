import pandas as pd

def find_missing_data(df):
    missing_values = df[df[['Latitude', 'Longitude']].isna().any(axis=1)]
    return missing_values



