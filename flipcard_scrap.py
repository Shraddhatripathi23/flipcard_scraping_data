#!/usr/bin/env python
# coding: utf-8



pip install pandas 
pip install bs4
pip install requests


import requests
from bs4 import BeautifulSoup

phn_nm=[]
phn_pr=[]

page_num=input("Enter number of pages")
for i in range (1, int (page_num)+1):
    url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi ="+str(i)
    req=requests.get (url)
    content=BeautifulSoup (req. content,"html.parser")
    name=content.find_all('div', {"class": "_4rR01T"})
    price=content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
    print("Phone in page "+str(i))
    print(len(name))
    
    
    for i in name:
        phn_nm.append(i.text)
    for i in price:
        phn_pr.append(i.text)


for i in phn_pr:
    print(i)

import pandas as pd
print(len(phn_pr), len(phn_nm))
data = {"phone name":phn_nm,"phone price":phn_pr}
df=pd.DataFrame(data)
print(df)







