import requests
import sys
import bs4
import re

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
month=[10,11]
def TCH():
    month=[10,11]
    list1=list()
    for m in month:
        url="https://www.tcmg.com.tw/register/register_1_detail.php?deptID=MODERNA&deptName=Covid-19%E7%96%AB%E8%8B%97%EF%BC%8A%E8%8E%AB%E5%BE%B7%E7%B4%8D&month={}&year=2021".format(month)
        rep=requests.get(url,headers={
            "user-agent":UA
        })
        rep=rep.text
        root=bs4.BeautifulSoup(rep,'html.parser')
        titles=root.find_all("td",valign="top")

        for title in titles : 
            date=title.text
            r=re.compile(r'^[0-9]{1,2}.*[\u4e00-\u9fa5].*')
            name=r.findall(date)
            for a in name:
                list1.append(a)
    return list1

            # for quota in title : 
            #     if title != None :
            #         print(title)
TCHm=TCH()                

if len(TCHm) != 0 :
    print(str(TCHm).replace(",","\n").strip(']').strip('[').strip(' '))
#     return list1    
#             # print(url) 
# TCHlist=TCH()

# if len(TCHlist) != 0:
#     print(TCHlist)

