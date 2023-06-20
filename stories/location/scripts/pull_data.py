# Start of Scripts
import pandas as pd

def load_data(file_path):
    # get dataframe
    #....
    # load data artifact
    data = pd.read_csv(file_path)
    return data
