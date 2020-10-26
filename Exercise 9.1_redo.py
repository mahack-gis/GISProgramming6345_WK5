#!/usr/bin/env python
# coding: utf-8

# In[1]:


file = open('words.txt', 'r')    #locates the file and 'r' reads each line
f = file.readlines()

#print(f)


# In[4]:


newList = []        #creates an empty list
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
        
#print(newList)


# In[5]:


longWords = []     #creates an empty list
for word in newList:         #traverse each word in newList
    if len(word) >= 20:       #if word is > 20 char add to new list
        longWords.append(word)
        
print(longWords)

