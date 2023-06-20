# Start of main script
import pandas as pd
from scripts.script_1 import split_date
from scripts.script_2 import analyze_csv_files  
import os

def main():
    URL = 'https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv'

    df = pd.read_csv(URL)
    # df = df[df['Document Type'] == "Journals"].sort_values(by='Internal ID')
    df = df[df['Text Only Transcript'].notnull()]

    
    # Split the data by date and save to csv
    date_df = split_date(df)

    output_directory = 'stories/date/data'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_text_date_path = os.path.join(output_directory, 'text_date.csv')
    date_df.to_csv(output_text_date_path, index=False)

    print("Data saved successfully.")
    
    # Define the directory where the csv files are saved
    directory = 'C:/Users/tyler/WWP_CS/engineering/Engineering_Repo/stories/date/data/'
    
    # Call the function to analyze each csv file
    analyze_csv_files(directory)


if __name__ == '__main__':
    main()
