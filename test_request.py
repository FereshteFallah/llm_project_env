#!/usr/bin/env python
# coding: utf-8

# In[10]:




import requests

url = "http://127.0.0.1:5000/generate"
data = {"text": "  امروز هوا"}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
