#!/usr/bin/env python
# coding: utf-8

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[12]:


st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == "s":
        print(word)


# In[5]:


for splitup in st:
    if st == st.split("s:"):
        print(splitup)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[17]:


for num in range(0,11,2):
    print(num)

#Code Here


# In[18]:


#Code in this cell
mylist = [x for x in range(1,51) if x%3==0]
mylist


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[20]:


st = 'Print every word in this sentence that has an even number of letters'


# In[21]:


for shadow in st.split():
    if len(shadow)%2==0:
        print(shadow)
    
        
        #Code in this cell


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[4]:


mylist = range(0,101)

for num in mylist:
    if num %3==0 and num%5==0:
        print("Fizzbuzz")
    elif num %5==0:
        print("Buzz")
    elif num %3==0:
        print("Fizz")
    else:
        print(num)
        
    
    

#Code in this cell


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[5]:


st = 'Create a list of the first letters of every word in this string'


# In[7]:


[word[0] for word in st.split()] 
    #Code in this cell

