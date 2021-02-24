#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np


# In[59]:


print(os.path.exists('/Users/chizzymba/Desktop/data science/jose portila course/Refactored_Py_DS_ML_Bootcamp-master/IMDb movies.csv'))


# In[60]:


df=pd.read_csv(r'/Users/chizzymba/Desktop/data science/jose portila course/Refactored_Py_DS_ML_Bootcamp-master/IMDb movies.csv')


# In[61]:


df.head() #view of what the dataset looks like


# In[62]:


df1 = pd.read_csv(r'/Users/chizzymba/Desktop/data science/jose portila course/Refactored_Py_DS_ML_Bootcamp-master/IMDb movies.csv')


# In[63]:


df2= pd.read_csv(r'/Users/chizzymba/Desktop/data science/jose portila course/Refactored_Py_DS_ML_Bootcamp-master/IMDb ratings.csv')


# In[64]:


df2.head()


# In[65]:


new_df = pd.merge(df1, df2, on = 'imdb_title_id') #merging the two datasets. 


# In[66]:


df.dtypes #checking for the data types within the data set


# In[67]:


df.memory_usage() 


# In[68]:


df['year'].unique() 
#this identifies one inncorrect record that has to be fixed either by replacing the record or dropping the row


# In[69]:


df[df['year']=='TV Movie 2019'] #to identify the unique id of the row with the problem


# In[70]:


df.drop(83917, axis=0, inplace= True) #dropping the row with the incorrect record


# In[71]:


df['year1']=df['year'].apply(np.int64)
df['year2']=df['year'].apply(np.float64)
df['year3']=df['year'].apply(np.str)
df.dtypes
#brief test to see how the memory is affected by differnt data types of the same size


# In[72]:


df.memory_usage() #clearly no difference in this case


# In[73]:


df['year'].astype(int)


# In[57]:


df[df.notnull()]


# reformating the year colum to int

# In[75]:


Year = df['year'].astype(int) 


# In[76]:


Year.head()


# In[77]:


df.insert(5, 'Year', Year)


# In[78]:


df.head()


# In[79]:


#df.drop(['year'], axis=1,inplace = True)


# In[80]:


cols = list(df1.columns.values)
cols


# In[85]:


df.columns


# In[86]:


df4= df[['imdb_title_id', 'title', 'date_published', 
       'duration', 'avg_vote','country', 'language', 'director', 'Year', 'genre','writer',
       'production_company', 'actors','original_title', 'description',  'votes',
       'budget', 'usa_gross_income', 'worlwide_gross_income', 'metascore',
       'reviews_from_users', 'reviews_from_critics']]
# to remove the duplicate year column and leave only the corect formated Year column


# In[87]:


df4.head() 


# sorting the dataset by year to get the first 10 records in 2020 to which i introduced some intentional errors and used within the chapter 3 of thesis

# In[88]:


df5 = df4.sort_values(by=['Year'], ascending= False).head(10)
df5


# In[89]:


df6=df5.loc[84749:53592,:'genre']


# In[90]:


df6.dtypes #to check what type of data type date_published is


# In[91]:


df6['Year']=df6['Year'].apply(np.int64)


# In[92]:


df6['year_check']=pd.DatetimeIndex(df6['date_published']).year


# In[93]:


df6.head()


# In[94]:


df6.drop('year__consitency_check', axis=1,  inplace= True)


# In[95]:


df6.at[78575, 'Year'] = 2021
df6.at[84574, 'Year'] = 2019
df6


# In[96]:


a=np.where(df6['Year'] != df6['year_check'], 'False','True')
#print ("inconsistency found in the year column for the movie" + df6['title'] )


# In[97]:


a


# In[98]:


df6['comparison column'] = np.where(df6['Year'] != df6['year_check'], 'False','True')


# In[99]:


df6


# In[103]:


df6['comparison_column'] = np.where(df6['Year'] != pd.DatetimeIndex(df6['date_published']).year, 'False','True')


# In[104]:


df6


# In[ ]:




