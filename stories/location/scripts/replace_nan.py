
# import pandas as pd

# def replace_nan_with_geolocation(df):
#     worldcities_df = pd.read_csv('stories/location/data/lookup/worldcities.csv')
#     gb_df = pd.read_csv('stories/location/data/lookup/gb.csv')
#     for index, row in df.iterrows():
#         # 'Name' is already a list of locations
#         locations = [name.strip() for name in row['Name']]
#         # go through each location from back to front
#         for location in reversed(locations):
#             try:
#                 #clara's method
#                 print('HI')
#             except:
#                 try:
#                     # Try to match with city_ascii in worldcities_df
#                     match = worldcities_df[worldcities_df['city_ascii'] == location].iloc[0]
#                     df.at[index, 'Latitude'] = match['lat']
#                     df.at[index, 'Longitude'] = match['lng']
#                     break  # If match is found, break the loop
#                 except:
#                     try:
#                         # Try to match with city in gb_df
#                         match = gb_df[gb_df['city'] == location].iloc[0]
#                         df.at[index, 'Latitude'] = match['lat']
#                         df.at[index, 'Longitude'] = match['lng']
#                         break  # If match is found, break the loop
#                     except:
#                         try:
#                             #API
#                             print('HI')
#                         except:
#                             continue  # If no match is found, continue to the next location
#         else:  # If no matches found after checking all locations
#             df.at[index, 'Latitude'] = ":("
#             df.at[index, 'Longitude'] = ":("
#     return df


import pandas as pd

def replace_nan_with_geolocation(df):
    worldcities_df = pd.read_csv('stories/location/data/lookup/worldcities.csv')
    gb_df = pd.read_csv('stories/location/data/lookup/gb.csv')
    for index, row in df.iterrows():
        locations = row['Name']  # 'Name' is already a list of locations
        for location in reversed(locations):
            loc_parts = [part.strip() for part in location.split(',')]  # Split location into its parts
            try:
                if len(loc_parts) == 3:
                    # We have city, state, and country
                    city, state, country = loc_parts
                    match = worldcities_df[(worldcities_df['city_ascii'] == city) &
                                           (worldcities_df['admin_name'] == state) &  # Update these to match your actual column names
                                           (worldcities_df['country'] == country)].iloc[0]
                elif len(loc_parts) == 2:
                    # We have only state and country
                    state, country = loc_parts
                    match = worldcities_df[(worldcities_df['admin_name'] == state) &
                                           (worldcities_df['country'] == country)].iloc[0]
                else:
                    # We have only country
                    country = loc_parts[0]
                    match = worldcities_df[worldcities_df['country'] == country].iloc[0]
                df.at[index, 'Latitude'] = match['lat']
                df.at[index, 'Longitude'] = match['lng']
                break
            except:
                df.at[index, 'Latitude'] = ":("
                df.at[index, 'Longitude'] = ":("
                continue
        else:  # If no matches found after checking all locations
            df.at[index, 'Latitude'] = ":("
            df.at[index, 'Longitude'] = ":("
    return df
