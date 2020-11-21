#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


df = pd.read_csv("all_data.csv")


# In[3]:


df.head()


# In[7]:


df.Country.nunique()


# In[9]:


sns.lineplot(data=df, x="Year", y="GDP", hue="Country")
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)
plt.title("GDP of Countries Between 2000 & 2015")


# In[24]:


ax = sns.lineplot(data=df, x="Year", y="Life expectancy at birth (years)", hue="Country")
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)
plt.title("Life Expectancy of Countries Between 2000 & 2015")
ax.set_xticks = range(1, 17, 1)
ax.set_axis_labels = range(2000, 2017)


# In[19]:


ax = sns.barplot(data=df, x="Country", y="GDP", hue="Year")
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)
plt.title("GDP of Countries")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")


# In[35]:


sns.relplot(data=df, x="Life expectancy at birth (years)", y="GDP", hue="Country", size="Year")
sns.set_style("darkgrid")


# In[ ]:




