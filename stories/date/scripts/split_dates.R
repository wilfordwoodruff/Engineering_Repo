library(tidyverse)
library(dplyr)
library(stringr)
library(stringi)
library(lubridate)

# Loading in the data
raw <- read_csv("https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv")
View(raw)

# FILTERS
all_journals <- raw %>% 
  filter(`Document Type` == "Journals")
View(all_journals)


sorted <- all_journals %>% 
  arrange(`Parent ID`)
view(sorted)

# Grab Text
n_full_text <- paste(sorted$`Text Only Transcript`, collapse = "")

# Grab Patterns
pattern_trey <- "(([J|F|M|A|J|S|O|N|D][a-z]{2,8}\\s){1,2}\\d{1,2}(th|st|rd|nd)?,?(\\s\\d{4})?|[J|F|M|A|J|S|O|N|D][a-z]{3,8}\\s\\d{1,2}(th|st|rd|nd)?) ~"

# Removing of the dates
matches <- str_extract_all(n_full_text, pattern=pattern_trey) %>% unlist()
matches2 <- append(matches, NA, after = 0)

# This then resplits the data by date as opposed by page
text <- strsplit(n_full_text, split = pattern_trey) %>% unlist()

# This creates our database which is huge for us
papers <- data.frame(
  date = matches2,
  text = text
)


# tilda removing 
papers$date <- substring(papers$date, 1, nchar(papers$date) - 1)

papers%>%mutate(date_new = unlist(format(mdy(papers$date), "%m/%d/%Y")))

view(papers)

papers()

