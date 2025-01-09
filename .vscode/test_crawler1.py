import requests
from bs4 import BeautifulSoup
from URL import url_manager
import re

root="http://www.douban.com/top250"
#pattern=r'^http://www.crazyant.net/\d+.html$'

urlmanager=url_manager()

urlmanager.add_url(root)

fout=open("python.txt","a",encoding="UTF-8")

while urlmanager.has_url():
    url=urlmanager.get_url()
    r=requests.get(url,timeout=5)
    if r.status_code!=200:
        print("error")
        continue
    r.encoding="utf_8"
    soup=BeautifulSoup(r.text,"html.parser")

    links=soup.find("ol",class_="grid_view").find_all("div",class_="hd").find("a")
    for link in links:
        href=link.get("href")
        if href==None:
            continue
        urlmanager.add_url(href)
        title=soup.title.string
        fout.write("%s\t%s\n"%(url,title))
        fout.flush()
        print("success:%s,%s"%(url,title))

fout.close()