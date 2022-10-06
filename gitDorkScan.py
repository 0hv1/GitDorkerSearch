import requests 
import os

sf=input("Enter Searching For: ")
st=input("Enter Searching Content Type: ")
pth= "allDorks.txt"
df=open(pth,"r")
df=str(df.read()).split("\n")
ldf=list(df)
mf="ms.txt"
mf=open(mf,"r")
mf=str(mf.read()).split("\n")
lmf=list(mf)
for dorks in ldf:
	for mf1 in lmf:
		print("https://github.com/search?q=%22"+sf+"%22%20"+dorks+"&type="+st)
		print("https://github.com/search?q=%22"+sf+"%22:"+dorks+"&type="+st)
		print("https://github.com/search?q=%22"+mf1+":"+sf+"%22%20"+dorks+"&type="+st)
		print("https://github.com/search?q=%22"+mf1+"%20"+sf+"%22%20"+dorks+"&type="+st)
