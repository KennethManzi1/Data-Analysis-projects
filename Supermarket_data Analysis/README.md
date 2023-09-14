# Supermarket sales Analysis

<img src="https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/ed12d855-b1ac-40dc-840f-410349c48d91" alt="Image" width="500" height="520">


## Table of Contents
- [Business Task](#business-task)
- [Solution and Code](#Solution-and-Code)
- [Link to the CSV file](#Link-to-the-CSV-file)

***

## Business Task
- Data Analysis on the super market sales CSV file acquired from the Kaggle website.
- We will be using multiple libraries in this project which will help us in analysing and visualizing our dataset.
- We will analyze many variables within this data set such as weekly sales across each city and Total sales per gender based on the product line
- Visualizations such as bar graphs, scatterplots, and line graphs were used to generate insights to compare key areas weekly sales gross price vs income.

***

## Solution and Code

- My analysis and findings are found in my Python Jupyter notebook [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/Supermarket_data%20Analysis/Kaggle%20Super%20Market%20Analysis.ipynb)
- My Original Python code created in Spyder can be found [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/Supermarket_data%20Analysis/Supermarketanalysis.py)


***

## Analysis 

- First we will begin to import the necessary libraries that we will need to conduct the analysis. These libraries are Pandas, Numpy, Matplotlib for the visualizations and also seaborn for the visualizations as well

```Python
#Importing the Libraries
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
  
- Next we will get the Supermarket Sales Csv and looking at the information available
```Python
sup_dat = pd.read_csv('/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_p
sup_dat
sup_dat.info()
sup_dat.describe()
```
![Screen Shot 2023-09-14 at 2 22 51 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/32d8a1d2-dbd2-4b30-a674-adc3ef9721b6)

##

- We will check for any Null Values
```Python
sup_dat.isnull()
```
![Screen Shot 2023-09-14 at 2 24 59 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/13acbea5-2a9a-4e75-bc88-9860f6e3169d)

Here we can see that there are no Null values within the data set

##
- Counts of the sales based on the product line and City
```Python
sup_dat['Product line'].value_counts()
sup_dat['City'].value_counts()
```
![Screen Shot 2023-09-14 at 2 29 02 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/551fbd90-e210-4319-ad04-20f28f9a98c5)


##

- Analyzing the relationship between the product price vs the gross income variables using a scatter plot

```Python
plt.figure(figsize=(10, 10))
x = sup_dat['Unit price']
y = sup_dat['gross income']
plt.scatter(x, y, color = 'magenta')
plt.xlabel('Unit Price')
plt.ylabel('Gross Income')
plt.title('Comparing Unit Price and Gross Income', fontsize = 10)
plt.show()
```
![Screen Shot 2023-09-14 at 2 58 37 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/84eb11fd-35b7-4d81-875f-f12fbb51a979)

- Based on the scatterplot, we can see a positive correlation between Unit Price and Gross Income.
- As the Unit Price goes up, so does the Gross Income and Vice Versa.

##

- Analyzing number of male and female data contributions within the dataset and creating a pie chart to illustrate the data 
```Python
count_gender = sup_dat['Gender'].value_counts()
Female_count = count_gender['Female']
Male_count = count_gender['Male']
label = ['Female', 'Male']

print('Number of Male:', Male_count)
print('Number of Female:', Female_count)

Male_ratio = Male_count/(Male_count+Female_count)
print('Male Ratio is', Male_ratio)
Female_ratio = Female_count/(Male_count+Female_count)
print('Female Ratio is ', Female_ratio)

plt.pie([Female_ratio, Male_ratio], labels=label)
plt.title('Male and Female Ratio', fontsize = 20)
plt.show()
```

![Screen Shot 2023-09-14 at 3 00 59 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/0ba3cfb2-7b2e-4b21-b904-e024b97fc56d)


#
- How many Sales done in each City?
```Python
cities = sup_dat['City']
City_counts = sup_dat['City'].value_counts()
Yangon_count = City_counts['Yangon']
naypyitaw_count = City_counts['Naypyitaw']
mandalay_count = City_counts['Mandalay']

x = ['Yangon', 'Naypyitaw', 'Mandalay']
y= [Yangon_count, naypyitaw_count, mandalay_count]
#fig, ax = plt.subplots()
plt.bar(x, y, label = ['red', 'blue', 'orange'], color = ['tab:red', 'tab:blue', 'tab:orange'])
plt.xlabel('Cities')
plt.ylabel('Sales done')
plt.show()
print(Yangon_count,
naypyitaw_count,
mandalay_count)

```
![Screen Shot 2023-09-14 at 3 05 50 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/9713d727-d03b-450d-9ad6-20d4284d99a2)

- Based on the visual, we can see that Yangon has the highest number of sales at 340.

#
- How many sales per Product line?
```Python
prod_line = sup_dat['Product line']
prodline_counts = sup_dat['Product line'].value_counts()
Fashion_accessories_count = prodline_counts['Fashion accessories']
food_beverages_count = prodline_counts['Food and beverages']
Electronic_accessories_count = prodline_counts['Electronic accessories']
Home_lifestyle_count = prodline_counts['Home and lifestyle']
Health_beauty_count = prodline_counts['Health and beauty']
sports_travel_count = prodline_counts['Sports and travel']

x = ['Fashion accessories', 'Food and beverages', 'Electronic accessories ',
     'Home and lifestyle','Health and beauty', 'Sports and travel']

y = [Fashion_accessories_count,food_beverages_count, Electronic_accessories_count,
     Home_lifestyle_count, Health_beauty_count, sports_travel_count]
plt.figure(figsize=(15, 10))
plt.bar(x, y, label = ['red', 'blue', 'orange', 'green', 'red', 'orange'], color = ['tab:red', 'tab:blue', 'tab:orange', 'tab:green','tab:red','tab:orange'])
plt.xlabel('Product Line')
plt.ylabel('Sales done')
plt.title('Sales done per product line')
plt.show()


```


![Screen Shot 2023-09-14 at 3 14 08 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/cfe8a370-76d8-4029-9862-2c6594cca44d)

- From the graph, we can see that the product line with the highest number of sales is Fashion Accessories at 175


#
- Next we will be updating the date and time columns to their proper data types as we will need them to create time series visuals with a line graph.
```Python
sup_dat['Date'] = pd.to_datetime(sup_dat['Date'])
sup_dat['Time'] = pd.to_datetime(sup_dat['Time'])
sup_dat.info()
```
![Screen Shot 2023-09-14 at 3 36 09 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/35ae5613-8b7d-4bfe-8cca-822cd866e577)


```Python
sup_dat.head()
```
![Screen Shot 2023-09-14 at 3 37 20 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/6eb16a10-0fdf-494b-a258-6ee4a6d5e899)


#
- Next we will group the total number of sales by the week
```Python
weekly_sales = sup_dat.groupby(['City', pd.Grouper(key='Date', freq='W')])['Total'].sum().reset_index()
weekly_sales
```
![Screen Shot 2023-09-14 at 3 38 42 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/82d956f4-2f85-40ba-933f-bea5459698a5)

- Bar graph of total number of sales per city 

```Python
plt.figure(figsize=(15, 10))
x = weekly_sales['City']
y = weekly_sales['Total']
plt.bar(x, y)
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.title('Total Sales Per City')
plt.grid(True)
plt.show()
```

![Screen Shot 2023-09-14 at 3 39 39 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/8ac9a6ba-4d43-480d-87e1-7c8c587b7a99)

- The city with the highest total number of sales is Mandalay

#

- Line graph of total number of sales per city by the week

```Python
plt.figure(figsize=(15, 10))
x = weekly_sales['Date']
y = weekly_sales['Total']
l = weekly_sales['City']
sns.lineplot(x = 'Date', y = 'Total', hue = 'City', marker = 'o', data = weekly_sales)
plt.title('Total Sales per city by the week', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Total Sales', fontsize=16)
plt.grid(True)
plt.legend(title='City', title_fontsize='14', loc='upper right', fontsize='13', bbox_to_anchor=(1.15, 1))
plt.show()
```

![Screen Shot 2023-09-14 at 3 42 11 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/75f838b5-bb63-437b-bc2c-d4e8e8f7cbe7)

- Mandalay had a big spike of sales from End of February until early March then dropped all the way to April.
- End of April although all the sales of the cities dropped, Yangon still ended up as the city with the highest number of sales towards April

- Average Sales per City
```Python
avg_weekly_sales = weekly_sales.groupby(['City'])['Total'].mean().reset_index()
avg_weekly_sales
```

![Screen Shot 2023-09-14 at 3 46 25 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/99b5d7d2-ba66-47a4-a462-86f0f3e35759)

- Bar graph of Average number of sales by per city

```Python
plt.figure(figsize=(15, 10))
x = avg_weekly_sales['City']
y = avg_weekly_sales ['Total']
plt.bar(x, y)
plt.xlabel('City')
plt.ylabel('Avg Sales')
plt.title('Avg Sales per City')
plt.grid(True)
plt.show()
```


![Screen Shot 2023-09-14 at 3 47 34 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/dd2789d3-419a-4e00-a80c-60c31a9184ab)

#
- Next we will visualize the total weekly sales over time.

```Python
Sales_bydate = sup_dat.groupby('Date')['Total'].sum()
plt.figure(figsize=(15, 10))
x = Sales_bydate.index
y = Sales_bydate.values
plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Total Sales Over Time')
plt.show()
```

![Screen Shot 2023-09-14 at 4 08 38 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/80899976-e383-42e0-81a0-8a9a7b8f2e34)

- Lastly, we will analyze sales Per Gender based on the Product Line using a multiple Bargraph through sns

```Python
plt.figure(figsize=(15, 10))
x = sup_dat['Gender']
l = sup_dat['Product line']
sns.countplot(x = 'Gender', hue = 'Product line', data = sup_dat)
plt.legend(title='Product line', loc='upper right', bbox_to_anchor=(1.15, 1))
plt.xticks(rotation=45)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Sales per Gender based on the product line')
plt.show()

```



***

## Link to the CSV file
- The link to the Kaggle CSV file can be found [here](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales/code)
- I have also included the CSV [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/Supermarket_data%20Analysis/supermarketsales.csv)





