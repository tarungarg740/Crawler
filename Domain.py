#!/usr/bin/env python
# coding: utf-8

# In[8]:


from urllib.parse import urlparse


# In[9]:


def get_sub_domain(url):
    source=urlparse(url)
    return source.netloc


# In[10]:



def get_domain(url):
    sub_domain=get_sub_domain(url)
    domain=sub_domain.split(".")
    #print(len(domain))
    if(len(domain)  >= 2) :
        str_= domain[-2] +"."+domain[-1]
        return str_
    else :
        return 0
    
    
    


# In[11]:




# In[ ]:




