library(readr)
library(stringr)
library(lubridate)
library(dplyr)

# Load CSV file from GitHub
url <- "https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv"
data <- read_csv(url)

filtered<- data %>% 
  filter(`Document Type` == "Journals")
View(filtered)

# Sorting the journals so they are more or less in order of when they were written
sorted <- filtered %>% 
  arrange(`Parent ID`)
view(sorted)

# Assuming 'Text Only Transcript' is the column you want to turn into one long string
n_full_text <- paste(sorted$`Text Only Transcript`, collapse = "")


process_dates <- function(input_text) {
  # Define date pattern
  date_pattern <- "(([J|F|M|A|J|S|O|N|D][a-z]{2,8}\\s){1,2}\\d{1,2}(th|st|rd|nd)?,?(\\s\\d{4})?|[J|F|M|A|J|S|O|N|D][a-z]{3,8}\\s\\d{1,2}(th|st|rd|nd)?) ~"
  
  # Extract dates based on pattern
  dates_extracted <- str_extract_all(input_text, pattern = date_pattern) %>% unlist()
  
  # Remove trailing tildas and format to "mm/dd/yyyy"
  dates_formatted <- dates_extracted %>% 
    str_remove(" ~") %>% 
    str_replace_all(c("th" = "", "st" = "", "rd" = "", "nd" = "")) 
  
  # Convert to date
  date_conversion <- mdy(dates_formatted)
  
  # Check which dates failed to parse
  failed_dates <- dates_formatted[is.na(date_conversion)]
  
  if(length(failed_dates) > 0) {
    print(paste("Failed to parse the following dates:", paste(failed_dates, collapse = ", ")))
  }
  
  # Format to "mm/dd/yyyy"
  dates_final <- format(date_conversion, "%m/%d/%Y")
  
  return(dates_final)
}


# Use this function to process your text
dates_final <- process_dates(n_full_text)



view(dates_final)