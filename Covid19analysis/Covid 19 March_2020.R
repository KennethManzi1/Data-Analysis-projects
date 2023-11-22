#Covid 19 data analysis in R using March 2020 data

#Loading the readr, ggplot2, and dplyr packages
install.packages('readr')
install.packages('ggplot2')
install.packages('dplyr')
library(readr)
library(ggplot2)
library(dplyr)

# Read datasets/confirmed_cases_worldwide.csv into confirmed_cases_worldwide
confirmed_cases_worldwide <- read_csv('Visualizing COVID-19/datasets/confirmed_cases_worldwide.csv')
confirmed_cases_worldwide

#Line plot to visualize the confirmed cases throughout the world
# Draw a line plot of cumulative cases vs. date
# Label the y-axis
ggplot(confirmed_cases_worldwide, aes(date, cum_cases)) +
  geom_line() +
  ylab("Cumulative confirmed cases")

#China compared to the rest of the world
# Read in datasets/confirmed_cases_china_vs_world.csv
confirmed_cases_china_vs_world <- read_csv('Visualizing COVID-19/datasets/confirmed_cases_china_vs_world.csv')

# See the result
confirmed_cases_china_vs_world

# Draw a line plot of cumulative cases vs. date, colored by is_china
# Define aesthetics within the line geom
plt_cum_confirmed_cases_china_vs_world <- ggplot(glimpse(confirmed_cases_china_vs_world)) +
  geom_line(aes(date, cum_cases, color = is_china)) +
  ylab("Cumulative confirmed cases")

# See the plot
plt_cum_confirmed_cases_china_vs_world

#Annotating
who_events <- tribble(
  ~ date, ~ event,
  "2020-01-30", "Global  Health \nEmergency Declared",
  "2020-03-11", "Pandemic\n Declared",
  "2020-02-13", "China Reporting\n Change"
) %>%
  mutate(date = as.Date(date))

# Using who_events, add vertical dashed lines with an xintercept at date
# and text at date, labeled by event, and at 100000 on the y-axis
plt_cum_confirmed_cases_china_vs_world +
  geom_vline(aes(xintercept = date), data = who_events, linetype = "dashed") +
  geom_text(aes(date, label = event), data = who_events, y = 1e5)

#Adding a Trendline to China
# Filter for China, from Feb 15
china_after_feb15 <- confirmed_cases_china_vs_world %>%
  filter(is_china == "China", date >= "2020-02-15")

# Using china_after_feb15, draw a line plot cum_cases vs. date
# Add a smooth trend line using linear regression, no error bars
ggplot(china_after_feb15, aes(date, cum_cases)) +
  geom_line() +
  geom_smooth(method = "lm", se = FALSE) +
  ylab("Cumulative confirmed cases")

# How the rest ofthe world compare to Linear Growth
# Filter confirmed_cases_china_vs_world for not China
not_china <- confirmed_cases_china_vs_world %>%
  filter(is_china != "China")

# Using not_china, draw a line plot cum_cases vs. date
# Add a smooth trend line using linear regression, no error bars
plt_not_china_trend_lin <- ggplot(not_china, aes(date, cum_cases)) +
  geom_line() +
  geom_smooth(method = "lm", se = FALSE) +
  ylab("Cumulative confirmed cases")


# See the result
plt_not_china_trend_lin 

#Adding a Logarithmic scale
# Modify the plot to use a logarithmic scale on the y-axis
plt_not_china_trend_lin + scale_y_log10()

#Countries outside of China that have been hit hardest
confirmed_cases_by_country <- read_csv("Visualizing COVID-19/datasets/confirmed_cases_by_country.csv")
glimpse(confirmed_cases_by_country)

# Group by country, summarize to calculate total cases, find the top 10
top_countries_by_total_cases <- confirmed_cases_by_country %>%
  group_by(country) %>%
  summarize(total_cases = max(cum_cases)) %>%
  top_n(10, total_cases)

# See the result
top_countries_by_total_cases

#Plotting the hardest hit countries during March 2020
# Read in the dataset from datasets/confirmed_cases_top7_outside_china.csv
confirmed_cases_top7_outside_china <- read_csv("datasets/confirmed_cases_top7_outside_china.csv")

# Glimpse at the contents of confirmed_cases_top7_outside_china
glimpse(confirmed_cases_top7_outside_china)

# Using confirmed_cases_top7_outside_china, draw a line plot of
# cum_cases vs. date, colored by country
ggplot(confirmed_cases_top7_outside_china, aes(date, cum_cases, color = country)) +
  geom_line() +
  ylab("Cumulative confirmed cases")


