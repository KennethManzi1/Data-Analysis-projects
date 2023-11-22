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


