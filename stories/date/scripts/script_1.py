import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import os
'''
TODO: for journals Look at the HTML instead


'''
def parse_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%B %d, %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        pass

def extract_text_by_date(clean_jour_df):
    dates = []
    text = ''.join(clean_jour_df['Text Only Transcript'])

    # Find dates using regular expressions
    regex_dates = re.findall(r'\b\w{3,9} \d{1,2},? \d{4}|\b\w{3} \d{1,2}\b|\b\w{3,9} \d{1,2}[—-] \d{4}', text)
    # Parse dates using dateutil library
    parsed_dates = [parse_date(date) for date in regex_dates]

    # Split text with dates
    for date in parsed_dates:
        if date is not None:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            date_str = date_obj.strftime('%B %d, %Y ~ %A')
            date_text = text.split(date_str)
            text = date_text[-1]
            dates.append({'date': date_str, 'text': date_text[:-1]})

    # Append last text block
    dates[-1]['text'].append(text)

    return dates

def split_date(clean_jour_df):
    dates = extract_text_by_date(clean_jour_df)
    date_df = pd.DataFrame(dates)
    return date_df

def main():
    src_data = pd.read_csv('https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv')

    # Filter source data to only include journal entries
    jour_src_data = src_data[src_data['Document Type'] == "Journals"]

    # Sort journal entries by their internal ID and only keep non-null text transcripts
    jour_df = jour_src_data.sort_values(by='Internal ID')
    clean_jour_df = jour_df[jour_df['Text Only Transcript'].notnull()]

    date_df = split_date(clean_jour_df)

    output_directory = 'stories/date/data'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_text_date_path = os.path.join(output_directory, 'text_date.csv')
    # output_split_date_path = os.path.join(output_directory, 'split_date.csv')

    date_df.to_csv(output_text_date_path, index=False)
    # date_df.to_csv(output_split_date_path, index=False)

    print("Data saved successfully.")


if __name__ == '__main__':
    main()
