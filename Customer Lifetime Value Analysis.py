#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("C:/Users/Lenovo/OneDrive/Documents/customer_acquisition_data.csv")
print(data.head())


# In[2]:


fig = px.histogram(data, 
                   x="cost", 
                   nbins=20, 
                   title='Distribution of Acquisition Cost')
fig.show()


# In[3]:


fig = px.histogram(data, 
                   x="revenue", 
                   nbins=20, 
                   title='Distribution of Revenue')
fig.show()


# In[4]:


cost_by_channel = data.groupby('channel')['cost'].mean().reset_index()

fig = px.bar(cost_by_channel, 
             x='channel', 
             y='cost', 
             title='Customer Acquisition Cost by Channel')
fig.show()


# In[5]:


conversion_by_channel = data.groupby('channel')['conversion_rate'].mean().reset_index()

fig = px.bar(conversion_by_channel, x='channel', 
             y='conversion_rate', 
             title='Conversion Rate by Channel')
fig.show()


# In[6]:


revenue_by_channel = data.groupby('channel')['revenue'].sum().reset_index()

fig = px.pie(revenue_by_channel, 
             values='revenue', 
             names='channel', 
             title='Total Revenue by Channel', 
             hole=0.6, color_discrete_sequence=px.colors.qualitative.Pastel)

fig.show()


# In[7]:


data['roi'] = data['revenue'] / data['cost']
roi_by_channel = data.groupby('channel')['roi'].mean().reset_index()

fig = px.bar(roi_by_channel, 
             x='channel', 
             y='roi', title='Return on Investment (ROI) by Channel')
fig.show()


# In[8]:


data['cltv'] = (data['revenue'] - data['cost']) * data['conversion_rate'] / data['cost']

channel_cltv = data.groupby('channel')['cltv'].mean().reset_index()

fig = px.bar(channel_cltv, x='channel', y='cltv', color='channel',
             title='Customer Lifetime Value by Channel')

fig.update_xaxes(title='Channel')
fig.update_yaxes(title='CLTV')

fig.show()


# In[9]:


subset = data.loc[data['channel'].isin(['social media', 'referral'])]

fig = px.box(subset, x='channel', y='cltv', title='CLTV Distribution by Channel')

fig.update_xaxes(title='Channel')
fig.update_yaxes(title='CLTV')
fig.update_layout(legend_title='Channel')

fig.show()


# In[ ]:




