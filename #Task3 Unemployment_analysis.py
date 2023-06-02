#!/usr/bin/env python
# coding: utf-8

# # UNEMPLOYMENT ANALYSIS WITH PYTHON

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#in order to ignore warnings
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df1 = pd.read_csv("C:/Users/lakav/Downloads/Unemployment in India.csv")
df1


# In[3]:


df2 = pd.read_csv("C:/Users/lakav/Downloads/Unemployment_Rate_upto_11_2020.csv")
df2


# In[4]:


#using len to store lengths
df1_len=len(df1)
df1_len


# In[5]:


df2_len=len(df2)
df2_len


# In[6]:


df2.head()


# In[7]:


df2.info


# In[8]:


#observing if this dataset contains missings values or not
print(df2.isnull().sum())


# In[9]:


# rename all the columns
df2.columns=["States","Date" ,"Frequency" ,"Estimated Unemployment Rate" ,"Estimated Employed ",
             "Estimated Labour Participation Rate" ,"Region","longitude","latitude"]
df2


# VISUALIZATION

# In[10]:


#Look at the correlation between the features of this data
sns.set_style("whitegrid")
sns.heatmap(df2.corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
plt.title('Correlation Matrix')
plt.show()


# In[18]:


#Unemployment by region
sns.countplot(x='Region', data=df2)
plt.title("Indian Unemployment by Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.show()


# In[12]:


df2.corr()


# In[13]:


#Estimating the no.of employees  according to different regions of india
plt.figure(figsize=(10, 4))
plt.title("Indian Unemployment")

for region in df2["Region"].unique():
    subset = df2[df2["Region"] == region]
    sns.histplot(data=subset, x="Estimated Employed ", label=region, kde=True)

plt.legend(title="Region")
plt.xlabel("Estimated Employed ")
plt.ylabel("Count")
plt.show()


# In[14]:


#Estimating the unemployment rate according to different regions of india
plt.figure(figsize=(10, 4))
plt.title("Indian Unemployment")

for region in df2["Region"].unique():
    subset = df2[df2["Region"] == region]
    sns.histplot(data=subset, x="Estimated Unemployment Rate", label=region, kde=True)

plt.legend(title="Region")
plt.xlabel("Estimated Unemployment Rate")
plt.ylabel("Count")
plt.show()


# In[15]:


# to create a pairwise scatter plot matrix

sns.set(style="ticks")
sns.pairplot(df2, palette="husl")


# In[16]:


#creating a dashboard to anlyze the unemploymentrate of each indian state by region

df2.columns = ["States", "Date", "Frequency", "Estimated Unemployment Rate", "Estimated Employed",
               "Estimated Labour Participation Rate", "Region", "longitude", "latitude"]

figure = px.sunburst(df2, path=['Region', 'States'], values='Estimated Unemployment Rate',
                     color='Estimated Unemployment Rate', color_continuous_scale='RdYlGn',
                     title='Unemployment Rate in India')

figure.update_traces(textinfo='label+percent entry')

figure.show()


# COMPLETED
