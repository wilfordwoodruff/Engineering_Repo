import pandas as pd

def replace_nan_with_geolocation(df):
    worldcities_df = pd.read_csv('stories/location/data/lookup/worldcities.csv')
    gb_df = pd.read_csv('stories/location/data/lookup/gb.csv')
    
    for index, row in df.iterrows():
        # Assign ":(" to latitude and longitude before trying to find matches
        df.at[index, 'Latitude'] = ":("
        df.at[index, 'Longitude'] = ":("
        
        # 'Name' is already a list of locations
        locations = [name.strip() for name in row['Name']]
        
        # go through each location from back to front
        for location in reversed(locations):
            try:
                # Try to match with city_ascii in worldcities_df
                matches = worldcities_df[worldcities_df['city_ascii'] == location]
                
                if len(matches) > 1:  # if there are multiple matches
                    for idx, match in matches.iterrows():
                        # Check whether the last element in the locations list is a country or a state
                        if match['admin_name'] == locations[-1] or match['country'] == locations[-1]:  # match state or country
                            df.at[index, 'Latitude'] = match['lat']
                            df.at[index, 'Longitude'] = match['lng']
                            break
                else:
                    match = matches.iloc[0]
                    df.at[index, 'Latitude'] = match['lat']
                    df.at[index, 'Longitude'] = match['lng']
                break  # If match is found, break the loop
            except:
                try:
                    # Try to match with city in gb_df
                    matches = gb_df[gb_df['city'] == location]
                    
                    if len(matches) > 1:  # if there are multiple matches
                        for idx, match in matches.iterrows():
                            # Check whether the last element in the locations list is a country or a state
                            if match['admin_name'] == locations[-1] or match['country'] == locations[-1]:  # match state or country
                                df.at[index, 'Latitude'] = match['lat']
                                df.at[index, 'Longitude'] = match['lng']
                                break
                    else:
                        match = matches.iloc[0]
                        df.at[index, 'Latitude'] = match['lat']
                        df.at[index, 'Longitude'] = match['lng']
                    break  # If match is found, break the loop
                except:
                    continue  # If no match is found, continue to the next location
    return df
