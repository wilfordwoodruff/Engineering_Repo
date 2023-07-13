import unittest
import pandas as pd
import os
import warnings

class TestAutobiographiesData(unittest.TestCase):
    
    def setUp(self):
        self.file_path = '../Engineering_Repo/stories/date/data/main_dates_auto.csv'
        self.df_auto = pd.read_csv(self.file_path)

    def test_csv_file_exists(self):
        self.assertTrue(os.path.exists(self.file_path))

    def test_csv_file_not_empty(self):
        self.assertNotEqual(self.df_auto.shape[0], 0)
    
    def test_columns_exist(self):
        required_columns = ['Parent_ID', 'order_id', 'date', 'text', 'date_new']  # modify this list according to your requirements
        for col in required_columns:
            self.assertIn(col, self.df_auto.columns)

    def test_date_nan_values(self):
        if self.df_auto['date'].isna().any():
            warnings.warn('NaN values found in date column.')
            self.df_auto[self.df_auto['date'].isna()].to_csv('../Engineering_Repo/stories/date/test/data/Auto_date_nan_rows.csv', index=False)

    def test_date_new_nan_values(self):
        if self.df_auto['date_new'].isna().any():
            warnings.warn('NaN values found in date_new column.')
            self.df_auto[self.df_auto['date_new'].isna()].to_csv('../Engineering_Repo/stories/date/test/data/Auto_date_new_nan_rows.csv', index=False)

    def test_date_format(self):
        # Assuming date format is 'YYYY-MM-DD'
        date_format = self.df_auto['date'].str.match('\d{4}-\d{2}-\d{2}').all()
        self.assertTrue(date_format)

if __name__ == '__main__':
    unittest.main()
