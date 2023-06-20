import pandas as pd
import os

# Function to calculate summary statistics for each csv file
def summarize_csv(file_path):
    df = pd.read_csv(file_path)
    
    # Display basic info
    print(f"\nFile: {file_path}")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nInfo:")
    print(df.info())
    print("\nFirst five rows:")
    print(df.head())
    
    # Display column-wise info
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(f"Number of unique values: {df[col].nunique()}")
        print(f"Number of missing values: {df[col].isna().sum()}")

        if df[col].dtype in ['int64', 'float64']:
            print(f"Mean: {df[col].mean()}")
            print(f"Median: {df[col].median()}")
            print(f"Standard Deviation: {df[col].std()}")

# Function to find csv files and calculate their summary statistics
def analyze_csv_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            summarize_csv(os.path.join(directory, filename))

def main():
    # Directory where csv files are stored
    directory = 'C:/Users/tyler/WWP_CS/engineering/Engineering_Repo/stories/date/data/'
    
    analyze_csv_files(directory)

if __name__ == '__main__':
    main()
