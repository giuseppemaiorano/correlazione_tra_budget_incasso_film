#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


movies_df = pd.read_csv("movies.csv")
movies_df.head(10)


# In[11]:


# Rimuovo i valori mancanti dagli attributi "budget" e "gross"
movies_cleaned_df = movies_df.dropna(subset=['budget', 'gross'])
"
# Normalizzo "budget" e "gross" convertendoli in milioni
movies_cleaned_df['budget'] = movies_cleaned_df['budget'] / 1e6
movies_cleaned_df['gross'] = movies_cleaned_df['gross'] / 1e6

movies_cleaned_df[['budget', 'gross']].head(10)


# In[12]:


correlation = movies_cleaned_df[['budget', 'gross']].corr()
print(correlation)


# In[16]:


plt.figure(figsize=(10, 6))
sns.regplot(x='budget', y='gross', data=movies_cleaned_df, scatter=False, color='red')
plt.scatter(movies_cleaned_df['budget'], movies_cleaned_df['gross'], alpha=0.5)
plt.title('Correlazione tra budget e incassi dei film')
plt.xlabel('Budget (in milioni)')
plt.ylabel('Inasso lordo (in milioni)')
plt.grid(True)
plt.show()


# In[ ]:




