# import pandas as pd

# def replace_nan_with_geolocation(df):
#     worldcities_df = pd.read_csv('C:/Users/zeony/OneDrive/Documents/MATH 488/Engineering_Repo/stories/location/scripts/worldcities.csv')
#     gb_df = pd.read_csv('C:/Users/zeony/OneDrive/Documents/MATH 488/Engineering_Repo/stories/location/scripts/gb.csv')
#     for index, row in df.iterrows():
#         try:
#             match = worldcities_df[worldcities_df['city_ascii'] == row['Name']].iloc[0]
#             df.at[index, 'Latitude'] = match['lat']
#             df.at[index, 'Longitude'] = match['lng']
#         except:
#             try:
#                 match = gb_df[gb_df['city'] == row['Name']].iloc[0]
#                 df.at[index, 'Latitude'] = match['lat']
#                 df.at[index, 'Longitude'] = match['lng']
#             except:
#                 df.at[index, 'Latitude'] = ":("
#                 df.at[index, 'Longitude'] = ":("

#     return df

# import pandas as pd

# def replace_nan_with_geolocation(df):
#     worldcities_df = pd.read_csv('C:/Users/zeony/OneDrive/Documents/MATH 488/Engineering_Repo/stories/location/scripts/worldcities.csv')
#     gb_df = pd.read_csv('C:/Users/zeony/OneDrive/Documents/MATH 488/Engineering_Repo/stories/location/scripts/gb.csv')
#     for index, row in df.iterrows():
#         # parse 'Name' into a list of locations
#         locations = [name.strip() for name in row['Name'].strip("[]").replace("'","").split(',')]
#         # go through each location from back to front
#         for location in reversed(locations):
#             try:
#                 # Try to match with city_ascii in worldcities_df
#                 match = worldcities_df[worldcities_df['city_ascii'] == location].iloc[0]
#                 df.at[index, 'Latitude'] = match['lat']
#                 df.at[index, 'Longitude'] = match['lng']
#                 break  # If match is found, break the loop
#             except:
#                 try:
#                     # Try to match with city in gb_df
#                     match = gb_df[gb_df['city'] == location].iloc[0]
#                     df.at[index, 'Latitude'] = match['lat']
#                     df.at[index, 'Longitude'] = match['lng']
#                     break  # If match is found, break the loop
#                 except:
#                     continue  # If no match is found, continue to the next location
#         else:  # If no matches found after checking all locations
#             df.at[index, 'Latitude'] = ":("
#             df.at[index, 'Longitude'] = ":("
#     return df

import pandas as pd

def replace_nan_with_geolocation(df):
    worldcities_df = pd.read_csv('stories/location/data/lookup/worldcities.csv')
    gb_df = pd.read_csv('stories/location/data/lookup/gb.csv')
    for index, row in df.iterrows():
        # 'Name' is already a list of locations
        locations = [name.strip() for name in row['Name']]
        # go through each location from back to front
        for location in reversed(locations):
            try:
                # Try to match with city_ascii in worldcities_df
                match = worldcities_df[worldcities_df['city_ascii'] == location].iloc[0]
                df.at[index, 'Latitude'] = match['lat']
                df.at[index, 'Longitude'] = match['lng']
                break  # If match is found, break the loop
            except:
                try:
                    # Try to match with city in gb_df
                    match = gb_df[gb_df['city'] == location].iloc[0]
                    df.at[index, 'Latitude'] = match['lat']
                    df.at[index, 'Longitude'] = match['lng']
                    break  # If match is found, break the loop
                except:
                    continue  # If no match is found, continue to the next location
        else:  # If no matches found after checking all locations
            df.at[index, 'Latitude'] = ":("
            df.at[index, 'Longitude'] = ":("
    return df
