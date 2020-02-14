#!/usr/bin/env python
# coding: utf-8

# In[11]:

from Spider import * 
from Domain import *
from Queue import *


# In[13]:


project_name="Crawler"
home_page="https://www.cognizant.com/"
domain_name=get_domain(home_page)
spider=Spider(project_name,home_page,domain_name)
spider.find_link(home_page)
spider.to_crawl()
            
	   





