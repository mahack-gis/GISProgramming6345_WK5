#!/usr/bin/env python
# coding: utf-8

# In[5]:


t = [[1, 2], [3], [4, 5, 6]]    #creates a list of tuples

def nested_sum(t):     #function created to add numbers in list
    total = 0          #variable to store total
    for x in t:        #traverses the list
        total += sum(x)   #adds each int to the total
    return total


# In[6]:


print(nested_sum(t))

