import sys
from typing import Text
import json 
import requests
import sys
import bs4
import re 
import TCH 
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"

url="https://notify-api.line.me/api/notify"
code="5xuXzmLQ43Q6N3e5FSseyb"
token="VxnJzHiMwmpERL3Fsvulho21PS70MhjiJE1G6cqPXQr"
clientID="0U1fwMxACHi3TxjOSwH1XL"
clintSecret="ikC2XlmLXUo0tCnuWA0rMGBWzPgSZLcbTSKWBPUKjE6"

def NMM():
    url="https://www.nininono.co/products/%E9%BA%A5%E5%85%8B%E9%A2%A8"
    resp=requests.get(url,headers={
        "user-agent":UA,
    })

    resp=resp.text

    root=bs4.BeautifulSoup(resp,"html.parser")
    title=root.find("div",class_="title global-primary dark-primary")
    sale=root.find("div",class_="out-of-stock txt-sold-out")

    if "售完" not in sale.string:
        return { title.string : sale.text } 
def LC():



    list1=list()
    # Params="divCode=319L&divName=%E8%8E%AB%E5%BE%B7%E7%B4%8D%E7%96%AB%E8%8B%97%E6%96%BD%E6%89%93%E7%8%A8%BA&p=1"
    for page in range(1,5):

        url="https://ssl.landseed.com.tw/lishin/policlinic/policlinic0302.php?divCode=319L&divName=%E8%8E%AB%E5%BE%B7%E7%B4%8D%E7%96%AB%E8%8B%97%E6%96%BD%E6%89%93%E7%8%A8%BA&p={}".format(page)
        Response=requests.get(url,headers={
        "user-agent":UA,
                        # "cookie":"over18=1"
        })
        req=Response.text
    
        root=bs4.BeautifulSoup(req,"html.parser")
        titles=root.find_all("td",class_="tbcell")
        

        for a in titles:
            if a != None:
                    try:
                        price=a.find("div",class_="dr_cell").text.replace("\t","").replace("\n","").replace("\r","") 
                    except:
                        price=None
                    
                    if price != None and str(price).count('額滿') == 0 and str(price).count('已過') == 0 and str(price).count('休診') == 0:
                        list1.append(price)
                        
                
            
    return list1
    # try:
    #     Nextpage=root.find("button",string="下一頁")
    #     Nextpage=Nextpage["onclick"].replace("window.location.href=\"","").replace("\"","")
    #     return str(Nextpage.encode('utf-8')).replace("\'","").lstrip('b')

    # except:
    #     return str("/")
def PL():

    listpl=list()
    url="https://rms.sph.org.tw/RMSTimeTable.aspx?dpt=S0990H"
    Response=requests.get(url,headers={
    "user-agent":UA,
                    # "cookie":"over18=1"
    })
    req=Response.text
    root=bs4.BeautifulSoup(req,"html.parser")
    titles=root.find_all("td",align="left")

    for a in titles:
       if a != None:
            price=a.text
            regex=re.compile(r'^[0-9]{5}[\u4e00-\u9fa5]{2,3}.*')
            price=regex.findall(price)
            
            for Outpatient in price:
                if Outpatient != None and "額滿" not in Outpatient : 
                    parent=a.find_previous_siblings('td',style="width:160px;")
                     
                    listpl.append(parent[0].text)
                    listpl.append(price)
    return listpl

def cm():
    url="https://mall.userjoy.com/UJITMStore/buy/content.aspx?goods_id=19079921"
    Response=requests.get(url,headers={
    "user-agent":UA,
                    # "cookie":"over18=1"
    })
    req=Response.text
    root=bs4.BeautifulSoup(req,"html.parser")
    titles=root.find_all("label",id="l_stocknum")
    print(titles.text)


msg=list()
# NMMm=NMM()
# if NMMm != None:
#     msg.append(str(NMMm).replace(" ","").replace("\\n",""))

TCHm=TCH.TCH()  
if len(TCHm) != 0 : 
    msg.append("===天成醫院===")
    msg.append(str(TCHm).replace(",","\n").strip(']').strip('[').strip(' '))


PLm=PL()
if len(PLm) != 0:
    msg.append("===聖保祿===")
    msg.append(PLm)



LCm=LC()
if len(LCm) != 0:
    msg.append("===聯新===")
    msg.append(LCm)


if len(msg) != 0:
    msg=str(msg).replace(",","\n").replace("[","").replace("]","").replace("'","")
    print(msg)


    data = {
        'message':"\n{}".format(msg)
        }

    response = requests.post(url,data=data,headers={
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/x-www-form-urlencoded"
    })
    print(response.text)