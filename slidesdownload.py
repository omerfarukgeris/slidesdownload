#!/usr/bin/env python3
#-*-coding:utf-8-*-

#Ömer Faruk GERİŞ

import subprocess
import urllib.request
import sys

par=[""]
arg=sys.argv
url=""
filename=""
the_page=""


def helpp():
	print("\nThe first argument must be one of the following:")
	print("\t-u\t Url")
	print("\t-f\t Filename: the output pdf filename.\n\t\t Default filename is page title.")
	print("\t-h\t Help")
	print("\t:slidesdownload -u https://www.slideshare.net/... ")
	print("\t:slidesdownload -u https://www.slideshare.net/... -f Slide ")
	
def getUrl(page):
	begin= int(str(page).find("data-full=")+11)
	end= int(str(page).find("?",begin+15))
	x=""
	for i in range(begin,end):
		x+=str(page)[i]
	print("\n\tUrl find = "+x)
	x=x.replace("-1-1024.jpg","-*-1024.jpg")
	x=x.replace("-1-638.jpg","-*-638.jpg")
	x=x.replace("-1-320.jpg","-*-320.jpg")
	
	return x
 
def getTitle(page):
	if(filename != ""):
		print("\n\tFilename = "+filename)
		return filename
	begin= int(str(page).find("<title>")+7)
	end= int(str(page).find("</title>",begin+8))
	x=""
	for i in range(begin,end):
		if(str(page)[i]==" "):
			break
		x+=str(page)[i]
	print("\n\tFilename = "+x)
	return x
	

if(len(sys.argv)<3):
	print("Error.Missing parameter...")
	exit()
try:
	for a in range(1,len(sys.argv)):
		par.append(sys.argv[a])
		
	par.append("")

	for a in range(0,len(sys.argv)):
		
		if(par[a]=="-h"):
			helpp()
			raise Exception()
		elif(par[a]=="-u" and a!=len(sys.argv)):		
			url=par[a+1]
			
		elif(par[a]=="-f" and a!=len(sys.argv)):
			filename=par[a+1]
		elif(par[a].startswith("-")	):
			print("Error.Invalid parameter : ",par[a])
			exit()
		

except Exception:
	exit()
	
except:
	print("Error: There was a missing or invalid parameter.(Help -h)")
	exit()

try:
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	the_page = response.read()	
except:
	print("Error.Invalid url try again...")
	exit()
 
src=getUrl(the_page)

filename=getTitle(the_page) 


i=0
j=0
k=100

while(1): 
	try:
		i+=1
		 
			
		urllib.request.urlretrieve(src.replace("*",str(i)),"page"+str(i)+".jpg")
		
		sys.stdout.write("\r\t--- page"+str(i)+".jpg downloading     Total page= "+str(i)+" --- \t"+"*"*(int(i)%10)+" "*(10-(int(i)%10)))
		
		if(i==k):
			k+=100
			j+=1
			
			subprocess.run("convert $(ls *.jpg | sort -V ) "+name+"-"+str(j)+".pdf", shell=True, executable='/bin/bash')
			subprocess.run("rm $(ls *.jpg)", shell=True, executable='/bin/bash')
			
			
	except:
		print("\r\tTotal page = "+str(i-1)+" "*50)
		break



j+=1
print("\tDownload Complete  "+filename+".pdf")

try:	
	subprocess.run("convert $(ls *.jpg  | sort -V ) "+filename+"-"+str(j)+".pdf", shell=True,  executable='/bin/bash')
	subprocess.run("rm $(ls *.jpg) ", shell=True, executable='/bin/bash')
except:
	print("Error.Please try again....")

exit()
