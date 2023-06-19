#Start of main script
import pandas as pd
from scripts.script_1 import split_by_date


def main():
    URL = 'https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv'

    df = pd.read_csv(URL)
    split_by_date(df)




if __name__ == '__main__':
    main()