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

```
#Importing the Libraries
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
  
- Next we will get the Supermarket Sales Csv and looking at the information available
```
sup_dat = pd.read_csv('/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_p
sup_dat
sup_dat.info()
sup_dat.describe()
```
![Screen Shot 2023-09-14 at 2 22 51 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/32d8a1d2-dbd2-4b30-a674-adc3ef9721b6)

##

- We will check for any Null Values
```
sup_dat.isnull()
```
![Screen Shot 2023-09-14 at 2 24 59 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/13acbea5-2a9a-4e75-bc88-9860f6e3169d)

Here we can see that there are no Null values within the data set

##
- Counts of the sales based on the product line and City
```
sup_dat['Product line'].value_counts()
sup_dat['City'].value_counts()
```
![Screen Shot 2023-09-14 at 2 29 02 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/551fbd90-e210-4319-ad04-20f28f9a98c5)

nnn
***

## Link to the CSV file
- The link to the Kaggle CSV file can be found [here](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales/code)
- I have also included the CSV [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/Supermarket_data%20Analysis/supermarketsales.csv)





