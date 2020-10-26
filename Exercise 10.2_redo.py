#!/usr/bin/env python
# coding: utf-8

# In[2]:


t = [1, 2, 3]         #creates a variable with a list of numbers

def cumsum(t):           #function to create a cumulative sum of num in list
    total = 0             #variable that will contain the temp sum
    result = []           #creates a new empty list
    for i in range(0, len(t)):   #traverse the numbers in list t
        total = total + t[i]     #add num to total and loop to next num
        result.append(total)   #add new total to the list
    return result
print(cumsum(t))

