#!/usr/bin/env python
# coding: utf-8

# # 2-3.2 Intro Python
# # The Power of List Iteration (loops)
# - for in: **`for`** loop using **`in`**
# - ** for range: `for range(start,stop,step)`** 
# - more list methods: **`.extend()`, `+, .reverse(), .sort()`**      
# - strings to lists, **`.split()`**, and list to strings, **`.join()`**   
# 
# 
# ----- 
# 
# &gt;<font> <b>Student will be able to</b></font>  
# - Iterate through Lists using **`for`** with **`in`**
# - **Use `for range()` in looping operations**  
# - Use list methods **`.extend()`, `+, .reverse(), .sort()`**  
# - convert between lists and strings using  **`.split()`** and **`.join()`**

# #  
# <font> <b>Concepts</b></font>
# ##  `range(stop)`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bda2424d-4f25-4c0a-a77a-06384f3da8f2/Unit2_Section3.2a_range_stop.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bda2424d-4f25-4c0a-a77a-06384f3da8f2/Unit2_Section3.2a_range_stop.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### The range(*stop*) function creates a sequence  
# using 1 argument with range(*stop*)
# - deault start: 0
# - stop: stopping integer, does not process stop number
# ```python
# for count in range(10):
#   print(count)
# ```
# ### same as
# ```python
# for count in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#   print(count)
# ```
# 

# #  
# <font> <b>Examples</b></font>  
# ### range runs from `0` through the integer before `stop`

# In[1]:


# [ ] review and run example
for count in range(10):
  print(count)


# In[2]:


# review and run example
digits = range(10)
print("digits =", list(digits), "\n")

for count in digits:
    print(count)


# In[3]:


# [ ] review and run example
sub_total = 0
for item in range(10):
    sub_total += item
    print("sub_total:", sub_total)
print("Total =", sub_total)


# In[6]:


# [ ] review and run example
# print the first half of a spelling list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length of 1st half of list (must be int)
half_1 = int(len(spell_list)/2)

for word in range(half_1):
    print(spell_list[word])


# #  
# <font> <b>Task 1</b></font>
# 
# ## `range(stop)`

# In[12]:


# [ ] for x = 6, use range(x) to print the numbers 1 through 6
x = 6
for num in range (1,x+1):
    print(num)


# In[13]:


# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
result=1
for num in range(1,8):
    result=result*num
print(result)
    


# Use **`range(stop)`** to print the second half of spell_list below

# In[17]:


# [ ] print the second half of a spelling list using a range(stop) loop to iterate the list
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]

half_2=int(len(spell_list)/2)
for word in range(half_2+1,len(spell_list)):
    print(spell_list[word])


# #  
# <font> <b>Concepts</b></font>
# ##  `range(start,stop)`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/95d6c75a-ed37-4f50-9049-2a2c225f9499/Unit2_Section3.2b_range_start_stop.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/95d6c75a-ed37-4f50-9049-2a2c225f9499/Unit2_Section3.2b_range_start_stop.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### The range(*start,stop*) function creates a sequence
# using 2 arguments with range(*start,stop*)
# - start: starting integer value of a range loop
# - stop: stopping integer (second argument), does not process stop number 
# ```python
# for count in range(5,10):
#   print(count)
# ```
# 

# ###  
# <font> <b>Examples</b></font>  
# ### range runs from `start` integer through the integer before `stop`

# In[8]:


# [ ] review and run example
for count in range(5,10):
  print(count)


# In[18]:


# [ ] review and run example
sub_total = 0
temp = 0
for item in range(5, 11):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)


# In[19]:


# [ ] review and run example

spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length list 
spell_len = len(spell_list)
# find lenght of 1st half (aka - start of 2nd half)
half_1 = int(spell_len/2)

# print 2nd half list
for word in range(half_1,spell_len):
    print(spell_list[word])


# #  
# <font> <b>Task 2</b></font>
# 
# ##  `range(start,stop)`

# In[20]:


# [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
# [ ] print list five_fifteen
five_fifteen=[]
for num in range(5,16):
    five_fifteen.append(num)
print(five_fifteen)


# In[21]:


# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list
# output should include "February", "November", "Annual"
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for word in range(2,5):
    print(spell_list[word])


# In[23]:


# [ ] using code find the index of "Annual" in spell_list
# [ ] using range, print the spell_list including "Annual" to end of list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
loc=spell_list.index("Annual")
for word in range(loc,len(spell_list)):
    print(spell_list[word])


# #  
# <font> <b>Concepts</b></font>
# ##  `range(start,stop,step)`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4299f0e2-3dc2-4298-aff1-e2a0b013de6a/Unit2_Section3.2c_range_start_stop_step.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4299f0e2-3dc2-4298-aff1-e2a0b013de6a/Unit2_Section3.2c_range_start_stop_step.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### The range(*start,stop,step*) function creates a sequence
# using 3 arguments with range(*start,stop,step*)
# - start: starting integer value of a range loop
# - stop: stopping integer (second argument), does not process stop number 
# - step: skip value for each loop
# ```python
# for count in range(10,101,10):
#   print(count)
# ```
# 

# #  
# <font> <b>Examples</b></font>  
# ### range runs from `start` integer, skipping by `step`, through the largest `step` integer before reaching `stop`

# In[24]:


# [ ] review and run example
for count in range(25,101,25):
  print(count)


# In[25]:


# [ ] review and run example
sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)


# In[26]:


# [ ] review and run example printing the 1st and then every other word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for index in range(0,len(spell_list),2):
    print(spell_list[index])


# In[27]:


# [ ] review and run example casting range to list
odd_list = list(range(1,20,2))
print(odd_list)


# #  
# <font> <b>Task 3</b></font>  
# ## `range(start,stop,step)`

# In[28]:


# [ ] print numbers 10 to 20 by 2's using range

for num in range(10,21,2):
    print(num)




# In[31]:


# [ ] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20

for num in range (20,9,-1):
    print(num)


# In[33]:


# [ ] print first and every third word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for word in range(0,len(spell_list),3):
    print(spell_list[word])


# #  
# <font> <b>Task 4</b></font>  
# 
# ### Program: List of letters 
# - Input a word string (**word**)
# - find the string length of word 
# - **use range()** to iterate through each letter in word (can use to range loops)
# - Save odd and even letters from the word as lists
#   - **odd_letters**: starting at index 0,2,...
#   - **even_letters**: starting at index 1,3,...
# - print odd and even lists

# In[38]:


# [ ] complete List of letters program- test with the word "complexity"
word=input("please enter a word: ")
odd_letters=[]
even_letters=[]
for letter in range(0,len(word),2):
    odd_letters.append(word[letter])
print(odd_letters)
for letter in range(1,len(word),2):
    even_letters.append(word[letter])
print(even_letters)


# #  
# <font> <b>Task 5: fix the error</b></font>
# 

# In[34]:


# [ ] fix the error printing odd numbers 1 - 9
for num in range[1,10,2]:
    print(num)




# In[35]:


# [ ] fix the error printing odd numbers 1 - 9
for num in range(1,10,2):
    print(num)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977)   [Privacy &amp; cookies](https://go.microsoft.com/fwlink/?LinkId=521839)   © 2017 Microsoft
