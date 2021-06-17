#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)


# In[2]:


#create a path to the "players.csv"
path = os.path.join("../","ProjectOne","players.csv")
path


# In[ ]:


#print the dataframe
df = pd.read_csv(path)
df


# In[ ]:


#print first 5 rows
df.head()


# In[ ]:


index_col=0


# In[ ]:


# One method to listing all the column names
# by iterating through the list of column names 
for col_name in df.columns:
    print(col_name)


# In[ ]:


# Another method for the dataframe to 
# show all columns sorted listed in alphabetical order
sorted(df)


# In[ ]:


# To count the number of rows you can used shape[]
rows = df.shape[0]
cols = df.shape[1]


# In[ ]:


print("Rows: " + str(rows))
print("Columns: " + str(cols))


# In[ ]:


# Use the len() method to count rows and columns 
rows = len(df.axes[0])
cols = len(df.axes[1])
print("Rows: " + str(rows))
print("Columns: " + str(cols))


# In[ ]:


# Group dataset by the nations and show the number of 
# players in each nation
PlayersByCountry= df.groupby(["nationality"]).size().reset_index(name='# of players')
print(PlayersByCountry)


# In[12]:


# To sort from greatest to least 
Top10 = PlayersByCountry.sort_values(by='# of players', ascending=False)


# In[13]:


Top10


# In[14]:


# To get only the top 10 nations with the most players
Top10 = Top10.head(10)
Top10


# In[15]:


#Get the top 5 countries
Top5Bar = Top10.head(5)
Top5Bar


# In[16]:


# Display the bar chart with top 5 players
# and their countries in green
Top5Bar.plot.bar(x='nationality', y=None, color={"# of players": "green"})


# In[17]:


Top5=df[['short_name','wage_eur','overall']]


# In[18]:


Top5.head(5)


# In[19]:


Top5Players = Top5[['short_name','wage_eur']] 


# In[20]:


Top5Players


# In[21]:


Top5Players.head(5)


# In[22]:


Top = Top5Players


# In[23]:


Top


# In[24]:


TopBar2 = Top.head(5)
TopBar2


# In[25]:


TopBar2.plot.bar(x='short_name', y=None)


# In[33]:


GermanyTop10 = df.loc[df['nationality'] == 'Germany']


# In[34]:


GermanyTop10


# In[38]:


GroupedGermanyTop10 = GermanyTop10.sort_values(by='overall', ascending=False)


# In[70]:


GroupedGermanyTop10.head(10)


# In[49]:


Top5Players = GroupedGermanyTop10[['long_name','height_cm','weight_kg','wage_eur']]


# In[50]:


Top5Players


# In[61]:


Sorted = Top5Players.sort_values(by='weight_kg', ascending=False)


# In[62]:


Sorted


# In[63]:


Sorted1 = Top5Players.sort_values(by='height_cm', ascending=False)


# In[64]:


Sorted1


# In[65]:


Sorted2 = Top5Players.sort_values(by='wage_eur', ascending=False)


# In[66]:


Sorted2


# In[67]:


Sorted.head(5)


# In[68]:


Sorted1.head(5)


# In[69]:


Sorted2.head(5)


# In[80]:


#Short Name and Wages for Germany players 
SortedTop5Germany = GermanyTop10[['short_name','wage_eur']]
SortedTop5Germany


# In[72]:


SortedTop5Germany.head(5)


# In[73]:


# Descending order for great shooting skills
TopShootingGermany = GermanyTop10.sort_values(by='shooting', ascending=False)


# In[74]:


TopShootingGermany


# In[76]:


# Shows the shooting from descending order and the short names
SortedTopShootingGermany = TopShootingGermany[['short_name','shooting']]


# In[77]:


SortedTopShootingGermany


# In[78]:


Top5ShootingGermany = SortedTopShootingGermany.head(5)


# In[79]:


#Displays Top 5 Shooters from Germany
Top5ShootingGermany


# In[81]:


TopDefensivePlayers = df[['short_name','defending','nationality','club']]


# In[82]:


TopDefensivePlayers


# In[83]:


SortedTopDefensivePlayers = TopDefensivePlayers.sort_values(by='defending', ascending=False)
SortedTopDefensivePlayers


# In[83]:


SortedTopDefensivePlayers = TopDefensivePlayers.sort_values(by='defending', ascending=False)
SortedTopDefensivePlayers


# In[84]:


Top5DefensivePlayers = SortedTopDefensivePlayers.head(5)
Top5DefensivePlayers


# In[ ]:


RealMadrid = df.loc[df['club'] == 'Real Madrid']


# In[ ]:


RealMadrid


# In[2]:


SortedRealMadrid = RealMadrid[['long_name','wage_eur']]
SortedRealMadrid


# In[1]:


OrderedSortedRealMadrid = SortedRealMadrid.sort_values(by='wage_eur', ascending=False)


# In[ ]:


SortedRealMadrid1 = RealMadrid[['long_name','shooting']]
SortedRealMadrid1


# In[ ]:


OrderedSortedRealMadrid1 = .SortedRealMadrid1.sort_values(by='shooting', ascending=False)
OrderedSortedRealMadrid1                                         


# In[ ]:


Top5ShootingMadrid = OrderedSortedRealMadrid1.head(5)
Top5ShootingMadrid


# In[ ]:


SortedRealMadrid2 = RealMadrid[['long_name','defending']]
SortedRealMadrid2


# In[ ]:


OrderedSortedRealMadrid2 = SortedRealMadrid2.sort_values('defending', ascending=False)
OrderedSortedRealMadrid2


# In[ ]:


Top5DefendingMadrid = OrderedSortedRealMadrid2.head(5)
Top5ShootingMadrid


# In[ ]:


SortedRealMadrid3 = RealMadrid[['long_name','nationality']]
SortedRealMadrid3


# In[ ]:


OrderedSortedRealMadrid3 = SortedRealMadrid3.sort_values(by='nationality', ascending=False)
OrderedSortedRealMadrid3 


# In[ ]:


Top5NationsMadrid = OrderedSortedRealMadrid3.head(5)
Top5NationsMadrid

