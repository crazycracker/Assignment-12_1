
# coding: utf-8

# # Problem Statement 12_1

# # 1

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[8]:


df['FlightNumber']


# In[12]:


df['FlightNumber'][1] = 10055
df['FlightNumber'][3] = 10075


# In[16]:


df['FlightNumber'] = df['FlightNumber'].astype('int')


# In[17]:


df['FlightNumber'].dtype


# # 2

# In[19]:


df[['From','To']] = df['From_To'].str.split('_',expand=True)


# In[20]:


df


# # 3

# In[ ]:


col_values = df['From'].values
converted_values = []

for col in col_values:
    converted_values.append(col.title())
df['From'] = converted_values

col_values = df['To'].values
converted_values = []

for col in col_values:
    converted_values.append(col.title())
df['To'] = converted_values


# In[32]:


df


# # 4

# In[34]:


#4 Delete from_to columns

df.drop(columns=['From_To'],inplace=True)


# In[37]:


df


# # 5

# In[74]:


#5 add new columns of delays

lists = df['RecentDelays'].values
max_size = 0
for lis in lists:
    max_size = max(max_size,len(lis))
max_size


# In[59]:


df


# In[81]:


df.drop(columns=['delay_1','delay_2','delay_3'],inplace=True)


# In[82]:


new_lists = list()
for x in range(1,4):
    new_vals = []
    for lis in lists:
        if len(lis) >= x:
            new_vals.append(lis[x-1])
        else :
            new_vals.append(np.nan)
    new_lists.append(new_vals)
df = df.assign(delay_1=new_lists[0])
df = df.assign(delay_2=new_lists[1])
df = df.assign(delay_3=new_lists[2])
df


# In[83]:


df.rename(columns={'RecentDelays':'Delays'},inplace=True)


# In[84]:


df

