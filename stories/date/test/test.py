# Start of test files
import pandas as pd
import datetime as dt

def test_data():
    # Load the data
    df = pd.read_csv('stories/date/data/main_dates_jour.csv')

    # Check that the DataFrame is not empty
    assert not df.empty, "DataFrame is empty"

    # Check that certain columns exist
    assert 'Parent_ID' in df.columns, "Parent ID column missing"
    assert 'date' in df.columns, "date column missing"
    assert 'order_id' in df.columns, "order_id column missing"
    assert 'text' in df.columns, "text column missing"

    # Check that there are no null values in the 'date' column
    assert df['date'].isnull().sum() == 0, "Null values in date column"

    # Check that the dates are in the correct format (YYYY-MM-DD)
    assert pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce').notnull().all(), "Incorrect date format"

    # Check the 'Parent ID' column for any invalid values
    # (replace the condition with the actual condition for invalid values)
    assert (df['Parent ID'] > 0).all(), "Invalid Parent ID values"

    # Check that dates are within a certain range
    min_date = pd.to_datetime('1800-01-01')
    max_date = pd.to_datetime('1900-12-31')
    assert (pd.to_datetime(df['date']) >= min_date).all(), "Date less than minimum allowed date"
    assert (pd.to_datetime(df['date']) <= max_date).all(), "Date greater than maximum allowed date"

    print("All tests passed.")

# Run the tests
test_data()
