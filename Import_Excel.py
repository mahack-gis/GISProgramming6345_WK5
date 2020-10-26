#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.read_excel('testPandas.xlsx')


# In[3]:


dataframe = pd.read_excel('testPandas.xlsx')
print(dataframe)


# In[4]:


dataframe.head(3)


# In[5]:


dataframe.plot.bar(x = 'Last', y = 'Age', rot = 0)

