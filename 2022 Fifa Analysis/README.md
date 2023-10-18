# FIFA 2022 Data Analysis

<img src="https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/57199a3d-2d7f-44bb-92a2-4895ea28685b" 
alt="Image" width="700" height="520">


## Table of Contents
- [Business Task](#business-task)
- [Solution and Code](#Solution-and-Code)
- [Analysis](#Analysis)
- [Link to the CSV file](#Link-to-the-CSV-file)

***

## Business Task

This is an exploratory data analysis on the Fifa 2022 dataset acquired from the Kaggle website and we will be using multiple Python libraries in this project such as Pandas and Seaborn that will help us in analysing and visualizing our dataset.

The FIFA22 dataset contains all key attributes, and features of male football players around the world. In this analysis, We will focus on key factors such as:
- The relationship between Potential & wages based on the clubs that are paying the wages.
- Potential & wages at the player level.
- Which nation is the most popular based on the number of players being represented.
- Which player earns the most per age group and potential level.
- Which club has the highest average of wages paid to their players





***

## Solution and Code

- My analysis and findings are found in my Python Jupyter notebook [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/2022%20Fifa%20Analysis/Fifa%202022%20analysis.ipynb)
- My Original Python code created in Spyder can be found [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/2022%20Fifa%20Analysis/Fifa2022Analysis.py)


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
- Next we will get the Fifa 2022 Csv and looking at the information available

```Python
fifadat2020 = pd.read_csv('/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/players22.csv', encoding_errors= 'replace')
fifadat2020
fifadat2020.head()
fifadat2020.describe()

```
![Screen Shot 2023-10-18 at 4 10 49 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/9b6cfcfa-a96f-469d-b996-398f2dc9a8ac)


##

- We will check for any Null Values
```Python
fifadat2020.isnull()
```
![Screen Shot 2023-10-18 at 4 12 01 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/b4be8760-fe8d-42ed-975a-22124a74ce24)

Here we can see that there are no Null values within the data set

##

- Dropping columns that we don't need
```Python
drop_columns = ['sofifa_id', 'player_url', 'long_name', 'dob', 'club_loaned_from',
                   'nation_position', 'nation_jersey_number', 'body_type', 'real_face',
                   'player_face_url', 'club_logo_url', 'nation_logo_url', 'nation_flag_url',
                    'goalkeeping_speed', 'player_tags', 'nation_team_id', 'club_flag_url']

new_fifadf = fifadat2020.drop(drop_columns, axis = 1)
new_fifadf
```
![Screen Shot 2023-10-18 at 4 14 12 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/079ad831-4daf-450c-a8f5-03190eb960bb)


##

**Relationship between player potential and wages**

- Here we will analyze the relationship between player potential and wages


***

## Link to the CSV file
- The link to the Kaggle CSV file can be found [here](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset/code)
- I have also included the CSV [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/2022%20Fifa%20Analysis/players22.csv)





