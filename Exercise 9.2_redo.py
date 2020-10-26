#!/usr/bin/env python
# coding: utf-8

# In[1]:


def has_no_e(word):      #creates a function called has_no_e
    for letter in word:     #traverses each letter in word
        if letter == 'e':       #if the letter is 'e' returns False
            return False
    return True                 #else it returns true


# In[2]:


has_no_e('star')     #'star' has no E so it should return True


# In[3]:


has_no_e('hello')    #'hello' has an E so it should return False


# In[4]:


file = open('testWords.txt', 'r')    #locates the file and 'r' reads each line
f = file.readlines()


# In[5]:


wordList = []        #creates an empty list
for line in f:
    if line[-1] == '\n':
        wordList.append(line[:-1])
    else:
        wordList.append(line)
        
print(wordList)


# In[6]:


##This attempt did not do what I expected:

noEWords = []     #creates an empty list
for word in wordList:         #traverse each word in newList
    for letter in word:     #traverses each letter in word
        if letter != 'e':       #if the letter is not 'e' add it to list
            noEWords.append(word)
            
print(noEWords)


# In[7]:


###found this solution online after several attempts on my own.
word = open('words.txt')
 
def words(word):      # function that takes a str
    wordCount = 0      #variable to hold the word count
    lineCount = 0      #variable to hold the line count
    for line in word:   #traverse each line in word
        if line.find('e') == -1:   #if the line has 'e'
            print(line)            #print it
            wordCount += 1         #incremeent word count by 1
        lineCount += 1             #increment line count by 1 for every line
    percent  = (float(wordCount) / float(lineCount)) * 100.0
    print(percent, '%')
 
words(word)

