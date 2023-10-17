#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 13:35:49 2023

@author: kennykaijage
"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fifadat2020 = pd.read_csv('/Users/kennykaijage/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Datasets/Datasets_for_projects/players22.csv', encoding_errors= 'replace')
fifadat2020

fifadat2020.info()


fifadat2020.head()

##Data Description
fifadat2020.describe()


#Finding any values that are Null

fifadat2020.isnull()

#Dropping columns that we don't need

drop_columns = ['sofifa_id', 'player_url', 'long_name', 'dob', 'club_loaned_from',
                   'nation_position', 'nation_jersey_number', 'body_type', 'real_face',
                   'player_face_url', 'club_logo_url', 'nation_logo_url', 'nation_flag_url',
                    'goalkeeping_speed', 'player_tags', 'nation_team_id', 'club_flag_url']

new_fifadf = fifadat2020.drop(drop_columns, axis = 1)
new_fifadf

#Relationship between player potential and wages

#Here we will analyze the relationship between player potential and wages

plt.figure(figsize=(7, 5))
sns.scatterplot(x = new_fifadf['potential'], y = new_fifadf['wage_eur'])
plt.xlabel("Potential") 
plt.ylabel("Wage EUR")
plt.title("Potential & wage", fontsize = 18)
plt.show()

#clubs 
new_fifadf['club_name']

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

#Next we will select the top 20 players and analyzing their statistics
top_21 = new_fifadf.nlargest(21, 'overall')
top_21

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

#Next we will analyze and research which Nationality is more popular than the others
national_counts = new_fifadf['nationality_name'].value_counts()
national_counts

#Creating a dictionary of the nationalities

from collections import Counter
bar_plot = dict(Counter(new_fifadf['nationality_name'].values).most_common(5))
bar_plot

#Bar plot
fig, ax = plt.subplots(figsize = (8,5))
plt.bar(*zip(*bar_plot.items()))
ax.set_title('Most Popular Nations')
plt.show()

#Average potential per nationality

avg_pot = new_fifadf.groupby('nationality_name')['potential'].mean().reset_index() 
avg_pot = avg_pot.sort_values(by='potential', ascending=False)
print(avg_pot)

#Plotting the averages
plt.figure(figsize=(20, 10))
avg_pot['nationality_name'] = avg_pot['nationality_name'].head(30)
sns.barplot(x= avg_pot['nationality_name'], y= avg_pot['potential'], palette='muted')
plt.title('Average Player Potential per Nationality')
plt.xlabel('nationality_name')
plt.ylabel('Average potential')
plt.xticks(rotation=45)
plt.show()

#Average Wages per Club

avg_wages = new_fifadf.groupby('club_name')['wage_eur'].mean().reset_index() 
avg_wages = avg_wages.sort_values(by='wage_eur', ascending=False)
print(avg_wages)


#Plotting the averages
plt.figure(figsize=(20, 10))
avg_wages['club_name'] = avg_wages['club_name'].head(30)
sns.barplot(x= avg_wages['club_name'], y= avg_wages['wage_eur'], palette='muted')
plt.title('Average Wages per team')
plt.xlabel('Club')
plt.ylabel('Average Wages')
plt.xticks(rotation=45)
plt.show()

#Top 12 Players and their wages by potential and by their age

players = new_fifadf[['short_name', 'wage_eur',
                  'overall','age',
                  'potential']].nlargest(12,['wage_eur']).set_index('short_name').sort_values(by = ['age'], ascending = False)

players

# Top 12 players overall

# We get the names and overals from the data
Overall_Rank = new_fifadf["overall"]
footballer = new_fifadf["short_name"]

# Let's create dataframe for the overall rank and the footballer
player_data = pd.DataFrame({'short_name': footballer,'overall':Overall_Rank})
player_data.set_index('short_name')

#x = new_fifadf['short_name'].head(20) 
#y = new_fifadf['overall'].head(20)

# plot
#plt.figure(figsize=(7,10))


#ax= sns.barplot(x=y, y=x, palette = 'Blues_r', orient='h')
#plt.xticks()
#plt.xlabel('Overall Ratings', size = 20) 
#plt.ylabel('Player Names', size = 20 ) 
#plt.title('FIFA22 Top 12 (Overall Rating)')

#plt.show()

# Distribution of players Ages

plt.hist(new_fifadf['age'], bins = 15)
plt.xlabel('Age of Players')
plt.ylabel('Number of Players')
plt.title('Distribution of Players Ages')

plt.tight_layout(pad=2)
plt.show()

# Distribution of players Wages

plt.hist(new_fifadf['overall'], bins = 20)
plt.xlabel('Overall status of player in the game')
plt.ylabel('Number of Players')
plt.title('Overall Status of Player')

plt.tight_layout(pad=2)
plt.show()