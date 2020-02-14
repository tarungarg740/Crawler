#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
    
    def length(self):
        return len(self.items)
    
    def to_print(self):
        print(self.items)





