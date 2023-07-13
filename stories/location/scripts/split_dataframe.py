import pandas as pd

def split_dataframe(df):
    new_df = df.copy()
    missing_values_df = new_df[new_df[['Latitude', 'Longitude']].isna().any(axis=1)]
    new_df.dropna(subset=['Latitude', 'Longitude'], inplace=True)
    
    return missing_values_df, new_df
