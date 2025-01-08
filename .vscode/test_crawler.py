import requests
from bs4 import BeautifulSoup
from URL import url_manager
import re

root="http://www.crazyant.net"
pattern=r'^http://www.crazyant.net/\d+.html$'

urlmanager=url_manager()

urlmanager.add_url(root)
#r=requests.get(root)

#print(urlmanager.get_url())

fout=open("python.txt","a",encoding="UTF-8")

while urlmanager.has_url():
    url=urlmanager.get_url()
    r=requests.get(url,timeout=10)
    if r.status_code!=200:
        print("error")
        continue
    r.encoding="utf_8"
    soup=BeautifulSoup(r.text,"html.parser")
    title=soup.title.string

    fout.write("%s\t%s\n"%(url,title))
    fout.flush()
    print("success:%s,%s"%(url,title))

    links=soup.find_all("a")
    for link in links:
        href=link.get("href")
        if href==None:
            continue
        if re.match(pattern,href):
            urlmanager.add_url(href)

    
fout.close()








# r.encoding="utf-8"

# html_cont=r.text

# soup=BeautifulSoup(html_cont,"html.parser")

# h2_node=soup.find_all("h2",class_="entry-title")

# for h2 in h2_node:
#     links=h2.find_all("a")
#     for link in links:
#        print(link.name,link["href"],link.get_text())




# img=soup.find("img")
# print(img["src"])