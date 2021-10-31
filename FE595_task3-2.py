#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data_g = pd.read_csv('webscrapenames')


# In[4]:


data_j = pd.read_csv('/Users/gloriarumao/OneDrive - stevens.edu/python/webscrapenames 2')


# In[5]:


data_a = pd.read_csv('Fontes_companyInfo.txt', delimiter = "\t")


# In[6]:


data_af = data_a.rename(columns={'0': 'Name', '1': 'Purpose'})


# In[7]:


data_s = pd.read_csv('3c.csv')


# In[8]:


data_sp = data_s.rename(columns={'name': 'Name', 'purpose': 'Purpose'})


# In[9]:


frames = [data_g,data_j, data_af, data_sp]
df = pd.concat(frames, ignore_index=True)


# In[10]:


df.shape[0]


# In[11]:


pd.set_option('display.max_rows', df.shape[0]+1)


# In[12]:


df


# In[13]:


from nltk.util import ngrams


# In[14]:


from nltk import word_tokenize


# In[15]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[16]:


analyser = SentimentIntensityAnalyzer()
Sentiment = list()
for purpose in df['Purpose']:
    Sentiment.append(analyser.polarity_scores(purpose))


# In[17]:


Sentiment


# In[18]:


len(Sentiment)


# In[19]:


df1 = pd.DataFrame()
df1 = df1.append(Sentiment, ignore_index=True, sort=False)


# In[20]:


df1


# In[21]:


df_new = pd.concat([df,df1], axis = 1, join = "inner")


# In[22]:


df_new


# In[23]:


#largest negative sentiment in Purpose
df_new.nlargest(5,['neg'])['Name']


# In[24]:


#smallest negative sentiment in Purpose
df_new.nsmallest(5,['neg'])['Name']


# In[25]:


#largest Positive sentiment in Purpose
df_new.nlargest(5,['pos'])['Name']


# In[26]:


#smallest positive sentiment in Purpose
df_new.nsmallest(5,['pos'])['Name']


# In[27]:


#largest Neutral sentiment in Purpose
df_new.nlargest(5,['neu'])['Name']


# In[28]:


#smallest Neutral sentiment in Purpose
df_new.nsmallest(5,['neu'])['Name']


# In[29]:


#largest Compound sentiment in Purpose
df_new.nlargest(5,['compound'])['Name']


# In[30]:


#smallest Compound sentiment in Purpose
df_new.nsmallest(5,['compound'])['Name']


# In[31]:


import collections
from textblob import TextBlob


# In[32]:


Sentiment2 = collections.defaultdict(list)
for purpose in df['Purpose']:
    blob = TextBlob(purpose)
    S = blob.sentiment
    Sentiment2['polarity'].append(S[0])
    Sentiment2['subjectivity'].append(S[1])


# In[33]:


df_new2 = pd.DataFrame(Sentiment2)


# In[34]:


df_new2


# In[35]:


df_new_2 = pd.concat([df,df_new2], axis = 1, join = "inner")


# In[36]:


df_new_2


# In[37]:


df_new_2.nlargest(5,['polarity'])['Name']


# In[38]:


df_new_2.nsmallest(5,['polarity'])['Name']


# ## Results: Top 5 companies

# ### Using nltk

# In[48]:


#largest Compound sentiment in Purpose
df_new.nlargest(5,['compound'])


# ### Using textblob

# In[46]:


df_new_2.nlargest(5,['polarity'])


# Since there are words like 'Coherent', 'Innovative','static' which have positive sentiment these company have high polarity with respect to textblob sentiment analysis.Wherelese most words in the purpose have neutral sentiment

# ## Bottom 5 companies

# ### Using nltk

# In[47]:


#smallest Compound sentiment in Purpose
df_new.nsmallest(5,['compound'])


# ### Using textblob

# In[49]:


df_new_2.nsmallest(5,['polarity'])


# Since there are words like 'Reduced','artificial','secondary' which have negative sentiment, and rest of the words in purpose have neutral sentiment the following results have lower polarity.

# In[ ]:




