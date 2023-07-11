import pandas as pd

def split_dataframe(df):
    new_df = df.copy()
    missing_values_df = new_df[new_df[['Latitude', 'Longitude']].isna().any(axis=1)]
    new_df.dropna(subset=['Latitude', 'Longitude'], inplace=True)
    
    # If new_df is empty after dropping rows with missing values, initialize it as an empty DataFrame with the same columns as df
    if new_df.empty:
        new_df = pd.DataFrame(columns=df.columns)
    
    return missing_values_df, new_df
