#!/usr/bin/env python
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from Domain import *
from Queue import *

class Spider:
    visited=[]
    project_name=''
    home_page=''
    domain_name=''
    global q
    q=Queue()
    
    def __init__(self,project_name,home_page,domain_name):
        
        self.project_name=project_name
        self.home_page=home_page
        self.domain_name=domain_name

    def find_link(self,url):
        try:
            source_content=requests.get(url).text
            soup=BeautifulSoup(source_content,"html.parser")
            for link in soup.find_all('a', href=True):
                if ((link['href'] not in q.items) and (link['href'] not in self.visited)):
                    q.enqueue((link['href']))
        except Exception as e:
            print(e)
        #print(q.length())
       
      


    def to_crawl(self):
        global i
        try:
            
                while not q.is_empty():
                    #print(i)
                    url = q.items[0]
                    print("\n",url)
                    str_=get_domain(url)
                    #print(str_)
                    if str_ == 'cognizant.com' :
                        if ".pdf" not in url and ".doc" not in url:
                            self.find_link(url)
                            #print(url)
                            self.scrapper(url)
                            if(q.length()==0):
                                break
                            print("----------------------------------")
                    self.visited.append(url)        
                    q.items.remove(url)
        except Exception as e:
            print(e)
    


    def scrapper(self,url):
        source_code = requests.get(url).text
        soup=BeautifulSoup(source_code,"html.parser")
        print(soup.title.text)
        for each_text in soup.find_all("p"):
            print(each_text.text)
            
         
        
    
        
           
   
