#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:30:29 2023

@author: kennykaijage
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

sup_dat = pd.read_csv('/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/supermarketsales.csv')
sup_dat

##Finding information of the super market spreadsheet including the data types for the columns

sup_dat.info()
##Data Description

sup_dat.describe()


#Finding any values that are Null

sup_dat.isnull()

##listing out the counts of different categories based on product line and city

sup_dat['Product line'].value_counts()
sup_dat['City'].value_counts()


##Analyzing the relationship between the product price vs the gross income variables using a scatter plot

plt.figure(figsize=(10, 10))
x = sup_dat['Unit price']
y = sup_dat['gross income']
plt.scatter(x, y)
plt.xlabel('Unit Price')
plt.ylabel('Gross Income')
plt.title('Comparing Unit Price and Gross Income', fontsize = 10)
plt.show()

#Analyzing number of male and female data contributions within the dataset and creating a pie chart to illustrate the data 
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

## How many sales done in each city
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
Yangon_count 
naypyitaw_count
mandalay_count 

##How many sales per Product line

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
     


#moving average of sales across the time frame of the dataset on a weekly basis
#Updating date and time columns to their data types
sup_dat['Date'] = pd.to_datetime(sup_dat['Date'])
sup_dat['Time'] = pd.to_datetime(sup_dat['Time'])
sup_dat.dtypes
sup_dat.head()

#Grouping the total number of sales by the week
weekly_sales = sup_dat.groupby(['City', pd.Grouper(key='Date', freq='W')])['Total'].sum().reset_index()
weekly_sales

#Bar graph of total number of sales per city by the week

plt.figure(figsize=(15, 10))
x = weekly_sales['City']
y = weekly_sales['Total']
plt.bar(x, y)
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.title('Total Sales Per City')
plt.grid(True)
plt.show()


#Line graph of total number of sales per city by the week

#plt.figure(figsize=(15, 10))
#x = weekly_sales['Date']
#y = weekly_sales['Total']
#l = weekly_sales['City']
#sns.lineplot(x, y, hue = l, marker = 'o')
#plt.title('Total Sales per city by the week', fontsize=20)
#plt.xlabel('Date', fontsize=16)
#plt.ylabel('Total Sales', fontsize=16)
#plt.grid(True)
#plt.legend(title='City', title_fontsize='14', loc='upper right', fontsize='13', bbox_to_anchor=(1.15, 1))
#plt.show()

#Average Sales per City
avg_weekly_sales = weekly_sales.groupby('City')['Total'].mean().reset_index()
avg_weekly_sales


#Bar graph of Average number of sales by per city

plt.figure(figsize=(15, 10))
x = avg_weekly_sales['City']
y = avg_weekly_sales ['Total']
plt.bar(x, y)
plt.xlabel('City')
plt.ylabel('Avg Sales')
plt.title('Avg Sales per City')
plt.grid(True)
plt.show()

#Line graph of total number of sales over time

Sales_bydate = sup_dat.groupby('Date')['Total'].sum()
plt.figure(figsize=(15, 10))
x = Sales_bydate.index
y = Sales_bydate.values
plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Total Sales Over Time')
plt.show()
