#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Create two list named list_sin and list_sin2
list_sin = [1,2,3,4,5,6]
list_sin2 = [9,8,7,6,5,5]


# In[15]:


# Concatenate the list_sin and list_sin2 into a new list called fin_list
fin_list = list_sin + list_sin2


# In[16]:


# Print the length of the fin_list
print("length of the fin_list",len(fin_list))


# In[17]:


# Find and print the maximum and minimum value of the fin_list
print("maximum value of fin_list",max(fin_list))
print("minimum value of fin_list",min(fin_list))


# In[18]:


# Calculate and print the sum of all the values in fin_list
print("sum of all the values in fin_list",sum(fin_list))


# In[19]:


# Reverse the order of the elements in the fin_list and print it
fin_list.reverse()
print("reverse the order",fin_list)


# In[ ]:




