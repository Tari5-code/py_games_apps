#!/usr/bin/env python
# coding: utf-8

# In[1]:


example = [0,1,2,3,4,5,6,7,8]


# In[2]:

from random import shuffle


# In[3]:


result = shuffle(example)


# In[4]:


result


# In[5]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[6]:


result = shuffle_list(example)


# In[7]:


result


# In[8]:


mylist = [' ', 'O', ' ']


# In[9]:


shuffle_list(mylist)


# In[10]:


def player_guess():
    
    guess = ''
    
    while guess not in ['0','1', '2']:
        guess = input("Pick a number: 0, 1 or 2")
    return int(guess)


# In[11]:


player_guess()


# In[12]:


myindex = player_guess()


# In[13]:


myindex


# In[14]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("correct!")
    else:
        print("wrong!")
        print(mylist)


# In[22]:


#INITIAL LIST
mylist = [' ', 'O', ' ']
#SHUFFLE LIST
mixed_up = shuffle_list(mylist)
#USER GUESS
guess = player_guess()
#CHECK GUESS
check_guess(mixed_up,guess)


# In[ ]:





# In[ ]:





# In[ ]:




