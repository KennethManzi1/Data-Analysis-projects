# Covid 19 Analysis using March 2020 Data.


<img src="https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/448404e7-9fdf-4057-9116-8dcd668d6684" 
alt="Image" width="700" height="520">



## Table of Contents
- [Business Task](#business-task)
- [Solution and Code](#Solution-and-Code)
- [Analysis](#Analysis)
- [Link to the CSV file](#Link-to-the-CSV-file)

***

## Business Task

In December 2019, COVID-19 coronavirus was first identified in the Wuhan region of China. By March 11, 2020, the World Health Organization (WHO) categorized the COVID-19 outbreak as a pandemic. A lot has happened in the months in between with major outbreaks in Iran, South Korea, and Italy.

We know that COVID-19 spreads through respiratory droplets, such as through coughing, sneezing, or speaking. But, how quickly did the virus spread across the globe? And, can we see any effect from country-wide policies, like shutdowns and quarantines?

Fortunately, organizations around the world have been collecting data so that governments can monitor and learn from this pandemic. Notably, the Johns Hopkins University Center for Systems Science and Engineering created a 
publicly available [data repository](https://github.com/RamiKrispin/coronavirus) to consolidate this data from sources like the WHO, the Centers for Disease Control and Prevention (CDC), and the Ministry of Health from multiple countries.

We will visualize COVID-19 data from the first several weeks of the outbreak to see at what point this virus became a global pandemic.

***

## Solution and Code

- My Original R code created in R Studio can be found [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/Covid19analysis/Covid%2019%20March_2020.R)

***

## Analysis 

- First we will begin to install and import the necessary libraries that we will need to conduct the analysis. These libraries are readr, ggplot2, and dplyr.

```R
install.packages('readr')
install.packages('ggplot2')
install.packages('dplyr')
library(readr)
library(ggplot2)
library(dplyr)
```
- Next we will load the dataset of the confirmed cases worldwide
```R
# Read datasets/confirmed_cases_worldwide.csv into confirmed_cases_worldwide
confirmed_cases_worldwide <- read_csv('datasets/confirmed_cases_worldwide.csv')

# See the result
confirmed_cases_worldwide
```
![Screen Shot 2023-11-22 at 3 35 17 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/b2e4f31e-ec71-4295-be18-56d243dec8f4)

- Now we will visualize the world wide cases using a lineplot based on the number of cases on the specific date
![Screen Shot 2023-11-22 at 3 37 30 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/a693372f-5f88-4c06-b5fa-1369765d6b5a)

![plot_zoom_png](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/5325911d-dc6d-4692-a365-d1f63aa1526b)

- From the line plot, we can see that the y-axis numbers are huge and terrifying, with the number of confirmed cases around the world during March 2020 getting close to 200,000. You can also see during February, the number of cases slightly dropped, then it drastically shoots upwards on March. We can dig deeper to further analyze that trend.
- Early on in the outbreak, the COVID-19 cases were primarily centered in China. Let's plot confirmed COVID-19 cases in China and the rest of the world separately to see if it gives us any insight.

```R
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
```
![Screen Shot 2023-11-22 at 3 43 44 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/836c8484-8efd-495a-8019-4ebf5234c399)

![plot_zoom_png](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/88d07328-21f3-4f17-8b3c-a9e3fad2aa20)

- The two lines have very different shapes. In February, the majority of cases were in China. That changed in March when it really became a global outbreak: around March 14, the total number of cases outside China overtook the cases inside China. This was days after the WHO declared a pandemic.
- There were a couple of other landmark events that happened during the outbreak. For example, the huge jump in the China line on February 13, 2020 wasn't just a bad day regarding the outbreak; China changed the way it reported figures on that day (CT scans were accepted as evidence for COVID-19, rather than only lab tests).
- By annotating events like this, we can better interpret changes in the plot.
```R
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
```
![Screen Shot 2023-11-22 at 4 22 41 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/96f9031b-965f-4254-b2a6-d5fc161bc541)

![plot_zoom_png](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/37b39d26-f405-4af3-b0c1-5c39f6ec9fad)

- Next We will Add a Trendline for China
```R
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

```
![Screen Shot 2023-11-22 at 4 29 42 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/1e6f16f6-8930-4e2e-8535-69744f0fd4f4)

![Screen Shot 2023-11-22 at 4 29 42 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/18c13a58-9942-4477-bb6d-7db40e503094)


- From the plot above, the growth rate in China is slower than linear. That's great news because it indicates China has at least somewhat contained the virus in late February and early March.

- Now we will see the rest of the world's linear growth
```R
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
```

![401fa44b-dd9c-4305-af70-9d6ab65b0e59](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/c4b9887d-dda9-41a3-ad01-3c4ed4fda766)

- From the plot above, we can see a straight line does not fit well at all, and the rest of the world is growing much faster than linearly. What if we added a logarithmic scale to the y-axis?

```R
# Modify the plot to use a logarithmic scale on the y-axis
plt_not_china_trend_lin + 
  scale_y_log10()
```
![29e8f863-5f93-48fc-8ce0-d2aca4d8561d](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/c7e246aa-72a3-4354-835a-79fc6b49e063)

- With the logarithmic scale, we get a much closer fit to the data. From a data science point of view, a good fit is great news.
- Unfortunately, from a public health point of view, that means that cases of COVID-19 in the rest of the world are growing at an exponential rate, which is terrible news.
- Not all countries are being affected by COVID-19 equally, and it would be helpful to know where in the world the problems are greatest.

```R
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
```

![Screen Shot 2023-11-22 at 4 35 46 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/633d6705-77fd-445d-89d8-ca55eaeb4744)

- Even though the outbreak was first identified in China, we can see South Korea in the above table. Four of the listed countries (France, Germany, Italy, and Spain) are in Europe and share borders.
- To get more context, we can plot these countries' confirmed cases over time.

```R
#Plotting the hardest hit countries during March 2020
# Read in the dataset from datasets/confirmed_cases_top7_outside_china.csv
confirmed_cases_top7_outside_china <- read_csv("Visualizing COVID-19/datasets/confirmed_cases_top7_outside_china.csv")

# Glimpse at the contents of confirmed_cases_top7_outside_china
glimpse(confirmed_cases_top7_outside_china)

# Using confirmed_cases_top7_outside_china, draw a line plot of
# cum_cases vs. date, colored by country
ggplot(confirmed_cases_top7_outside_china, aes(date, cum_cases, color = country)) +
  geom_line() +
  ylab("Cumulative confirmed cases")
```


![11ecc233-0d4b-49ca-afe2-3925d3d2aea0](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/026ab845-d6fc-4390-978c-a2ed0ba00a39)





