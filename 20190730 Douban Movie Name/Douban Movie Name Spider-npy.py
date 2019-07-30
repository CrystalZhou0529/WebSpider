import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import numpy as np

url='https://movie.douban.com/j/search_tags?type=movie&source=index'
headers={'user-agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
r=requests.get(url, headers=headers)
r.encoding='utf-8'
result=json.loads(str(r.text))
tags=result['tags']

movie=[]

for tag in tags:
    start=0
    while True:
        url='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&page_limit=50&page_start='+str(start)
        r=requests.get(url, headers=headers)
        r.encoding='utf-8'
        result=json.loads(str(r.text))
        result=result['subjects']
        for item in result:
            movie.append(item)
        
        if len(result)==0:
            break
        start+=50
        print(len(movie))
        
print(len(movie))
m=np.array(movie)
np.save('Douban Movie Name.npy', m)