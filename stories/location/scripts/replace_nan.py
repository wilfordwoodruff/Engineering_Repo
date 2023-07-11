import pandas as pd
import numpy as np

def replace_nan_with_zero(df):
    new_df = df.copy()
    new_df['Latitude'] = new_df['Latitude'].fillna(0)
    new_df['Longitude'] = new_df['Longitude'].fillna(0)
    return new_df
