#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd


# In[91]:


data_g = pd.read_csv('webscrapenames')


# In[92]:


data_j = pd.read_csv('/Users/gloriarumao/OneDrive - stevens.edu/python/webscrapenames 2')


# In[93]:


data_a = pd.read_csv('Fontes_companyInfo.txt', delimiter = "\t")


# In[94]:


data_af = data_a.rename(columns={'0': 'Name', '1': 'Purpose'})


# In[95]:


data_s = pd.read_csv('3c.csv')


# In[96]:


data_sp = data_s.rename(columns={'name': 'Name', 'purpose': 'Purpose'})


# In[97]:


frames = [data_g,data_j, data_af, data_sp]
df = pd.concat(frames, ignore_index=True)


# In[98]:


df.shape[0]


# In[49]:


pd.set_option('display.max_rows', df.shape[0]+1)


# In[99]:


df


# In[100]:


from nltk.util import ngrams


# In[101]:


from nltk import word_tokenize


# In[102]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[103]:


analyser = SentimentIntensityAnalyzer()
Sentiment = list()
for purpose in df['Purpose']:
    Sentiment.append(analyser.polarity_scores(purpose))


# In[104]:


Sentiment


# In[105]:


len(Sentiment)


# In[106]:


df1 = pd.DataFrame()
df1 = df1.append(Sentiment, ignore_index=True, sort=False)


# In[107]:


df1


# In[108]:


df_new = pd.concat([df,df1], axis = 1, join = "inner")


# In[109]:


df_new


# In[110]:


#largest negative sentiment in Purpose
df_new.nlargest(5,['neg'])['Name']


# In[111]:


#smallest negative sentiment in Purpose
df_new.nsmallest(5,['neg'])['Name']


# In[112]:


#largest Positive sentiment in Purpose
df_new.nlargest(5,['pos'])['Name']


# In[113]:


#smallest positive sentiment in Purpose
df_new.nsmallest(5,['pos'])['Name']


# In[114]:


#largest Neutral sentiment in Purpose
df_new.nlargest(5,['neu'])['Name']


# In[117]:


#smallest Neutral sentiment in Purpose
df_new.nsmallest(5,['neu'])['Name']


# In[115]:


#largest Compound sentiment in Purpose
df_new.nlargest(5,['compound'])['Name']


# In[116]:


#smallest Compound sentiment in Purpose
df_new.nsmallest(5,['compound'])['Name']


# In[118]:


import collections
from textblob import TextBlob


# In[119]:


Sentiment2 = collections.defaultdict(list)
for purpose in df['Purpose']:
    blob = TextBlob(purpose)
    S = blob.sentiment
    Sentiment2['polarity'].append(S[0])
    Sentiment2['subjectivity'].append(S[1])


# In[120]:


df_new2 = pd.DataFrame(Sentiment2)


# In[121]:


df_new2


# In[122]:


df_new_2 = pd.concat([df,df_new2], axis = 1, join = "inner")


# In[123]:


df_new_2


# In[124]:


df_new_2.nlargest(5,['polarity'])['Name']


# In[125]:


df_new_2.nsmallest(5,['polarity'])['Name']


# ## Results: Top 5 companies

# ### Using nltk

# In[127]:


#largest Compound sentiment in Purpose
df_new.nlargest(5,['compound'])[['Name','Purpose']]


# ### Using textblob

# In[128]:


df_new_2.nlargest(5,['polarity'])[['Name','Purpose']]


# ## Bottom 5 companies

# ### Using nltk

# In[129]:


#smallest Compound sentiment in Purpose
df_new.nsmallest(5,['compound'])[['Name','Purpose']]


# ### Using textblob

# In[130]:


df_new_2.nsmallest(5,['polarity'])[['Name','Purpose']]


# In[ ]:




