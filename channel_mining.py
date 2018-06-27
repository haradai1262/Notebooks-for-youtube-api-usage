
# coding: utf-8

# # Youtube Api V3 usage for channel mining
# 
# # Install 
# ### pip install --upgrade google-api-python-client
# ### pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
# ### pip install --upgrade oauth2client

# In[4]:


import sys, os
from pprint import pprint

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import devkey
DEVELOPER_KEY = devkey.api1

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

CHANNEL_ID = 'UCMsuwHzQPFMDtHaoR7_HDxg' # channel id of japanese popular (and cute) youtuber "Yukirinu"


# In[5]:


# build
YT = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
# search
feed = YT.search().list( channelId=CHANNEL_ID,
                        maxResults=50, order='date',
                        type='video',
                        part='id,snippet' ).execute()


# In[6]:


# check item
pprint( feed.get('items')[0] )


# In[7]:


for i, video in enumerate( feed.get('items') ):
    vid, title = video['id']['videoId'], video['snippet']['title']
    print( i, vid, title )


# In[ ]:


# pandasにしよう...

