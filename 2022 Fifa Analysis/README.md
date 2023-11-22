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

```Python
plt.figure(figsize=(7, 5))
sns.scatterplot(x = new_fifadf['potential'], y = new_fifadf['wage_eur'])
plt.xlabel("Potential") 
plt.ylabel("Wage EUR")
plt.title("Potential & wage", fontsize = 18)
plt.show()
```
![Screen Shot 2023-11-11 at 6 52 15 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/d37dcb37-0843-4976-a1e9-ba36d39d85fe)


From this scatterplot, we can see a positive correlation in the scatterplot between player potential and wages. In most cases, we can see that as the player's potential grows over time, so does their wages over time. We do see cases where the some of the player's wages remain the same while a couple others at mid 80s had a ridiculous high wage while a few 90s have a low wage.

This may depend on the club that they play in as most clubs especially premier league clubs don't pay that many high wages while big teams like Manchester City, Barcelona, Real Madrid, and PSG pay higher wages to their best and high potential stars.


```Python
#clubs 
new_fifadf['club_name']
```

```Python
#new_fifadf['club_names'] = new_fifadf.loc[new_fifadf['club_name' == 'Barcelona']]

#Filtering the dataset to analyze the player potential and wage for the top 8 teams.
selected_clubs = ['Liverpool', 'Manchester United', 'Manchester City', 'Real Madrid CF', 'Paris Saint-Germain', 'FC Barcelona',
                 'Chelsea', 'Juventus']

# Filter the DataFrame to include only the selected clubs
filtered_data = new_fifadf[new_fifadf['club_name'].isin(selected_clubs)]

plt.figure(figsize=(7, 5))
sns.scatterplot(x=filtered_data['potential'], y=filtered_data['wage_eur'], hue=filtered_data['club_name'])
plt.xlabel("Potential") 
plt.ylabel("Wage EUR")
plt.title("Potential & Wage for Selected Clubs", fontsize=18)
plt.show()

```

![Screen Shot 2023-10-18 at 4 41 47 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/7c9cf80b-56bc-4736-8c19-1db8a9b393b7)

From the scatterplot, we can see that Real Madrid, Manchester City, and PSG do pay high wages on the 350k mark for some of their high potential super stars. We can analyze further to compare the players and their wages.

##

**Next we will select the top 21 players and analyzing their statistics**


```Python
top_21 = new_fifadf.nlargest(21, 'overall')
top_21

#Comparing the 21 players and their wages

fig, ax = plt.subplots(figsize=(10,8))

plt.scatter(top_21['potential'], top_21['wage_eur'] )
plt.text(top_21.iloc[0]['potential'], top_21.iloc[0]['wage_eur'], top_21.iloc[0]['short_name'])
plt.text(top_21.iloc[1]['potential'], top_21.iloc[1]['wage_eur'], top_21.iloc[1]['short_name'])
#plt.text(top_21.iloc[2]['potential'], top_21.iloc[2]['wage_eur'], top_21.iloc[2]['short_name'])
plt.text(top_21.iloc[3]['potential'], top_21.iloc[3]['wage_eur'], top_21.iloc[3]['short_name'])
plt.text(top_21.iloc[4]['potential'], top_21.iloc[4]['wage_eur'], top_21.iloc[4]['short_name'])
plt.text(top_21.iloc[5]['potential'], top_21.iloc[5]['wage_eur'], top_21.iloc[5]['short_name'])
plt.text(top_21.iloc[6]['potential'], top_21.iloc[6]['wage_eur'], top_21.iloc[6]['short_name'])
plt.text(top_21.iloc[7]['potential'], top_21.iloc[7]['wage_eur'], top_21.iloc[7]['short_name'])
plt.text(top_21.iloc[8]['potential'], top_21.iloc[8]['wage_eur'], top_21.iloc[8]['short_name'])
plt.text(top_21.iloc[9]['potential'], top_21.iloc[9]['wage_eur'], top_21.iloc[9]['short_name'])
plt.text(top_21.iloc[10]['potential'], top_21.iloc[10]['wage_eur'], top_21.iloc[10]['short_name'])
plt.text(top_21.iloc[11]['potential'], top_21.iloc[11]['wage_eur'], top_21.iloc[11]['short_name'])
plt.text(top_21.iloc[12]['potential'], top_21.iloc[12]['wage_eur'], top_21.iloc[12]['short_name'])
plt.text(top_21.iloc[13]['potential'], top_21.iloc[13]['wage_eur'], top_21.iloc[13]['short_name'])
plt.text(top_21.iloc[14]['potential'], top_21.iloc[14]['wage_eur'], top_21.iloc[14]['short_name'])
plt.text(top_21.iloc[15]['potential'], top_21.iloc[15]['wage_eur'], top_21.iloc[15]['short_name'])
plt.text(top_21.iloc[16]['potential'], top_21.iloc[16]['wage_eur'], top_21.iloc[16]['short_name'])
#plt.text(top_21.iloc[17]['potential'], top_21.iloc[17]['wage_eur'], top_21.iloc[17]['short_name'])
plt.text(top_21.iloc[18]['potential'], top_21.iloc[18]['wage_eur'], top_21.iloc[18]['short_name'])
plt.text(top_21.iloc[19]['potential'], top_21.iloc[19]['wage_eur'], top_21.iloc[19]['short_name'])
plt.text(top_21.iloc[20]['potential'], top_21.iloc[20]['wage_eur'], top_21.iloc[20]['short_name'])

ax.set_title("Overall Rating vs Wages")
ax.set_ylabel('Wages')
ax.set_xlabel('Rating')

plt.show()
```

![Screen Shot 2023-10-18 at 4 48 29 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/2654d2ae-fd6b-45a5-9e28-310e17708f61)

In Fifa 2022, we can see that there is no relationship between wages and rating and the reason for this is that we can see that Mbappe has a 95 rating but is only making less than 250k while Benzema has an 89 rating and is making close to 350k a week

##

**Next we will analyze and research which Nationality is more popular than the others**

```Python
national_counts = new_fifadf['nationality_name'].value_counts()
national_counts
```

![Screen Shot 2023-10-18 at 4 50 03 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/2248c3fe-1407-41c3-8d4e-69522c141575)

```Python
#Creating a dictionary of the nationalities

from collections import Counter
bar_plot = dict(Counter(new_fifadf['nationality_name'].values).most_common(5))
bar_plot

```
![Screen Shot 2023-10-18 at 4 56 33 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/4fbfaef8-341e-4372-bee5-79241e59d80c)



```Python
fig, ax = plt.subplots(figsize = (8,5))
plt.bar(*zip(*bar_plot.items()))
ax.set_title('Most Popular Nations')
plt.show()

```

![Screen Shot 2023-10-18 at 4 57 11 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/62e43c07-e787-46ef-ac47-cb7752ecfdb2)


##
**Average Player Potential Rating per Nationality**

```Python
avg_pot = new_fifadf.groupby('nationality_name')['potential'].mean().reset_index() 
avg_pot = avg_pot.sort_values(by='potential', ascending=False)
print(avg_pot)
```

![Screen Shot 2023-10-18 at 5 03 48 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/29a3c126-37de-48ed-86ab-4a8454eaaa16)



```Python
#Plotting the averages
plt.figure(figsize=(20, 10))
avg_pot['nationality_name'] = avg_pot['nationality_name'].head(30)
sns.barplot(x= avg_pot['nationality_name'], y= avg_pot['potential'], palette='muted')
plt.title('Average Player Potential per Nationality')
plt.xlabel('nationality_name')
plt.ylabel('Average potential')
plt.xticks(rotation=45)
plt.show()
```

![Screen Shot 2023-10-18 at 5 03 59 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/a4afdc45-755a-4b16-9a1a-21e319c9f9e9)


##
**Average Wages Per Team**

```Python
#Average Wages per Club

avg_wages = new_fifadf.groupby('club_name')['wage_eur'].mean().reset_index() 
avg_wages = avg_wages.sort_values(by='wage_eur', ascending=False)
print(avg_wages)
```

![Screen Shot 2023-10-18 at 5 05 26 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/b99c3daf-d156-413a-8b83-7f3a6caa1d7b)


```Python
#Plotting the averages
plt.figure(figsize=(20, 10))
avg_wages['club_name'] = avg_wages['club_name'].head(30)
sns.barplot(x= avg_wages['club_name'], y= avg_wages['wage_eur'], palette='muted')
plt.title('Average Wages per team')
plt.xlabel('Club')
plt.ylabel('Average Wages')
plt.xticks(rotation=45)
plt.show()
```
![Screen Shot 2023-10-18 at 5 05 33 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/2fdfec94-1806-4aac-b97b-0d060d95b40a)


##
**Top 12 Players and their wages by potential and by their age**

```Python
players = new_fifadf[['short_name', 'wage_eur',
                  'overall','age',
                  'potential']].nlargest(12,['wage_eur']).set_index('short_name').sort_values(by = ['age'], ascending = False)

players
```
![Screen Shot 2023-10-18 at 5 07 36 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/4bf65cd9-dcf2-4934-8879-9627d169b981)


```Python
# Top 12 players overall

# We get the names and overals from the data
Overall_Rank = new_fifadf["overall"]
footballer = new_fifadf["short_name"]

# Let's create dataframe for the overall rank and the footballer
player_data = pd.DataFrame({'short_name': footballer,'overall':Overall_Rank})
player_data.set_index('short_name')
```

![Screen Shot 2023-10-18 at 5 08 32 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/8e4ad3ab-8631-409c-8dd1-4ee35dac9cf6)

```Python
#plotting the data 

x = new_fifadf['short_name'].head(12) 
y = new_fifadf['overall'].head(12)

# plot
plt.figure(figsize=(7,10))


ax= sns.barplot(x=y, y=x, palette = 'Purples_r')
plt.xticks()
plt.xlabel('Overall Ratings', size = 20) 
plt.ylabel('Player Names', size = 20 ) 
plt.title('FIFA22 Top 12 (Overall Rating)')

plt.show()
```

![Screen Shot 2023-10-18 at 5 09 30 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/762ce79a-e126-4228-912a-4de8ab162f38)


##
**We will now create histograms to analyze distributions within the age of the players and also another histogram to analyze frequencies within the overall status of players**

```Python
# Distribution of players Ages

plt.hist(new_fifadf['age'], bins = 15)
plt.xlabel('Age of Players')
plt.ylabel('Number of Players')
plt.title('Distribution of Players Ages')

plt.tight_layout(pad=2)
plt.show()
```

![Screen Shot 2023-10-18 at 5 11 41 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/5d9a1c4c-af32-4832-b9e7-b6d5a9596525)



```Python
# Distribution of players status

plt.hist(new_fifadf['overall'], bins = 20)
plt.xlabel('Overall status of player in the game')
plt.ylabel('Number of Players')
plt.title('Overall Status of Player')

plt.tight_layout(pad=2)
plt.show()
```
![Screen Shot 2023-10-18 at 5 12 32 PM](https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/18dcecd7-ef05-4a56-99a3-d554938110af)


Conclusion: This is such a fun data to work with. I am a big European Football guy especially Liverpool Football club. I'll do an analysis on Liverpool football Club data specifically at some point soon

**From this Analysis we can conclude that:**
- Messi is the best player.
- Manchester City, Real Madrid, and Paris Saint Germain pay their stars higher wages(250k+) to their high potential superstar players than most clubs.
- Kevin De Bryune is currently the highest paid player overall making 350k a week
- There's generally a positive relationship between players potential rating & wages.
- Majority of the players in Fifa 20 are in the 20-25 age range.
- Majority of the players overall status level is between 60-75.
- However among the top 21 sample of players that we took, that was not the case as we can see on that sample of players there was no correlation between those players potential rating and & wages. You can see Benzema with an 89 rating and Casemiro who is a CDM making way more money than Mbappe with 95+ rating.
- Real Madrid pays the highest wages on average to their players compared to other teams.
- Estonia has the highest potential average in the game compared to other nationalities.
- England have the most representation among countries in the data with Germany and Spain closely getting there but England still blows them out of the water.

***

## Link to the CSV file
- The link to the Kaggle CSV file can be found [here](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset/code)
- I have also included the CSV [here](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/2022%20Fifa%20Analysis/players22.csv)





