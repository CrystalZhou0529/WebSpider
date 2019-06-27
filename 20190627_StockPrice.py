import requests
import re
import bs4
from bs4 import BeautifulSoup
import pandas as pd

def getHTML(url):
    try:
        r=requests.get(url)
        #print(r.status_code)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("False HTML!")
        return ""

def getList(bbb,ulist):
    for i in range(4836):
        t=bbb[i].string
        lef=t.find('(')
        rig=t.find(')')
        if (t[lef+1]=='3') or (t[lef+1]=='6'):
            ulist.append([t[:lef], t[lef+1:rig]])
        #print(ulist[i])
    pass

def getPrice(ulist):
    for i in range(len(ulist)):
        origin='https://gupiao.baidu.com/stock/'
        if ulist[i][1][0]=='6':
            origin=origin+'sh'
        if ulist[i][1][0]=='3':
            origin=origin+'sz'
        if (ulist[i][1][0]!='3') and (ulist[i][1][0]!='6'):
            continue
        url=origin+ulist[i][1]+'.html'
        html=getHTML(url)
        try:
            soup=BeautifulSoup(html, 'html.parser')
            ccc=soup.find_all('strong')
            ulist[i].append(ccc[0].string)
            for sp in soup.strong.find_next_siblings():
                ulist[i].append(sp.string)
            #print(ulist[i])
        except:
            print('False: ', i)
            continue
    
def main():
    
    url = 'http://quote.eastmoney.com/stock_list.html'
    uhtml = getHTML(url)
    soup=BeautifulSoup(uhtml, 'html.parser')
    aaa=soup.find_all('div', {'class':'quotebody'})
    bbb=aaa[0].find_all('li')
    
    ulist=[]
    uinfo=[]
    getList(bbb,ulist)
    
    getPrice(ulist)
    ans=pd.DataFrame(ulist)
    ans.to_excel('StockPrice.xlsx')
    
main()