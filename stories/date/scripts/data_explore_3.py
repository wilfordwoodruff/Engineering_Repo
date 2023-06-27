import pandas as pd

df = pd.read_csv('stories/date/data/text_date_journals.csv')
# df = pd.read_csv('stories/date/data/text_date_full.csv')

print(df.head())

for i in range(10):
    print(df['date'][i])
    print('-----------------------------')
    print(df['text'][i])
    print('\n\n')




for i in range(len(df['date'])-10, len(df['date'])):
    print(df['date'][i])
    print('-----------------------------')
    print(df['text'][i])
    print('\n\n')






# URL = 'https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv'

# df = pd.read_csv(URL)

# print(df['Document Type'].unique())