from pull_data import load_data
from transform_data import transform_data
from save_data import save_data

def main(): 
    # Load data from CSV file
    file_path = "C:/Users/zeony/OneDrive/Documents/MATH 488/Engineering_Repo/stories/location/scripts/wwp_data.csv"
    location_dat = load_data(file_path) 
    
    # Transform the data 
    final_data = transform_data(location_dat)

    # Save data 
    save_data(final_data, "stories/location/data/final_data.csv")

if __name__ == '__main__': 
    main()