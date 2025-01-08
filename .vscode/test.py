import re

str=input()

if re.search(r'\w+@(qq)|(139)\.com',str):
    print("correct")
else:
    print("no")