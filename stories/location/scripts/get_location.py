import pandas as pd

def get_location_from_csv(df, csv_files):
    for csv_file in csv_files:
        df_csv = pd.read_csv(csv_file)
        for i, row in df.iterrows():
            if row['Name'] in df_csv['city'].values:
                df.at[i, 'Latitude'] = df_csv[df_csv['city']==row['Name']]['lat'].values[0]
                df.at[i, 'Longitude'] = df_csv[df_csv['city']==row['Name']]['lng'].values[0]
    return df
    