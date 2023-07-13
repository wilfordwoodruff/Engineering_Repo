library(tidyverse)
library(stringr)
library(lubridate)

# Load the data
raw <- read_csv("https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv")

# Filter for "Journals" in the Document Type column
all_journals <- raw %>% 
  filter(`Document Type` == "Journals")

# Define pattern to match dates
pattern_trey <- "(([J|F|M|A|J|S|O|N|D][a-z]{2,8}\\s){1,2}\\d{1,2}(th|st|rd|nd)?,?(\\s\\d{4})?|[J|F|M|A|J|S|O|N|D][a-z]{3,8}\\s\\d{1,2}(th|st|rd|nd)?) ~"

# Define function to process each row
process_row <- function(row) {
  matches <- str_extract_all(row$`Text Only Transcript`, pattern=pattern_trey) %>% unlist()
  matches2 <- append(matches, NA, after = 0)
  text <- strsplit(row$`Text Only Transcript`, split = pattern_trey) %>% unlist()
  data.frame(
    `Parent_ID` = row$`Parent ID`,
    order_id = row$Order,
    date = matches2,
    text = text
  ) %>%
    mutate(date = str_sub(date, end = -2),
           date_new = format(mdy(date), "%m/%d/%Y"))
}

# Apply function to each row of the dataframe and bind rows together
papers <- bind_rows(lapply(split(all_journals, 1:nrow(all_journals)), process_row))

# View the final dataframe
View(papers)

# Get current working directory
current_dir <- getwd()

# Build the path to the file
file_path <- file.path(current_dir, '../../stories/date/data/main_dates_jour.csv')

# Create the directory if it doesn't exist
dir.create(dirname(file_path), recursive = TRUE, showWarnings = FALSE)

# Write the data to a CSV file
write_csv(papers, file_path)

