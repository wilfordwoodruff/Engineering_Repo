import pandas as pd

def merge_dataframes(df_no_missing, df_filled):
    df_no_missing.reset_index(drop=True, inplace=True)
    df_filled.reset_index(drop=True, inplace=True)
    df_complete = pd.concat([df_no_missing, df_filled])
    return df_complete