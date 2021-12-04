import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
from dateutil.relativedelta import *
from datetime import *
from PyPDF2 import PdfFileReader
import io
from tika import parser
title =[]
title1=[]
description=[]
time=[]
time1=[]
author=[]
link=[]
link1=[]
tree=[]
def getDateList(startDate):
 today=datetime.now()
 dateList=[]
 while(startDate<today):
   dateList.append(startDate.strftime("%d%m%Y"))
   startDate=startDate+relativedelta(months=+3)
 #print("\n".join(map(str,dateList)))
 return dateList

tree=getDateList(datetime(1997,1,1))
print(tree)
year= "1997"

#url= "https://www.bis.org/list/cbspeeches/from_01012020/index.htm"
#results= requests.get(url)
#soup= BeautifulSoup(results.text, "html.parser")
headers= {"Accept-language": "en-US, en;q=0.5"}

for page in tree:
    print(page[-4:])
    print(year)
    if(page[-4:]!=year):
        link.append("this year ends")
        year=page[-4:]
        
    z= str(page)
    page= requests.get("https://www.bis.org/list/cbspeeches/from_" + z + "/index.htm", headers= headers)
    soup= BeautifulSoup(page.text, 'html.parser')
    movie_div = soup.find_all('tr', class_='item even')
    movie_div1=soup.find_all('tr', class_='item odd')
    sleep(randint(2,10))
    for x in movie_div:
    
   
       date= x.td.text
       time.append(date)

       titles = x.div.a.text
       title.append(titles)

       links= x.div.a
       link.append(links['href'])
    
    for y in movie_div1:
    
   
       date= y.td.text
       time.append(date)
    
       titles = y.div.a.text
       title.append(titles)

       links= y.div.a
       link.append(links['href'])
    

with open('listfile1.txt', 'w') as f:
    for item in link:
        f.write("%s\n" % item)

      

  
 
#print(time)
#print(title)
#print(link)


print("end of program")
