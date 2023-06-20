# save as csv or json to data
'''
TODO:
    1. Save the new location dataframe
    2. Combine the dataframes and save it
        1. Save for Journals first
        2. Save for all
'''

def save_data(data, filename): 
    # Saving final dataset 
    data.to_csv(filename, index=False)

