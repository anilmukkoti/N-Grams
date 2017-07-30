import sys
import os
from collections import OrderedDict
import collections
#function to genrate 3,5,7 grams respectively from a given file
def generator(threeg,fiveg,seveng,filename):
	sevg = {}
	for line in open(filename):
		line = line.rstrip()
		parts = line.split()
	
	le= len(parts) #total numbers in the text file
	# to find seven grams
	garam = []
	for k in range (0,le-6):
		if k == le-7 :
			gram = parts[k]+" "+parts[k+1]+" "+parts[k+2]+" "+parts[k+3]+" "+parts[k+4]+" "+parts[k+5]+" "+parts[k+6]
			garam = gram
			if gram in seveng:
				seveng[gram] += 1
			else:
				seveng[gram] = 1
			if gram in sevg:
				sevg[gram] += 1
			else:
				sevg[gram] = 1
		else :
			gram = parts[k]+" "+parts[k+1]+" "+parts[k+2]+" "+parts[k+3]+" "+parts[k+4]+" "+parts[k+5]+" "+parts[k+6]
			if gram in seveng:
				seveng[gram] += 1
			else:
				seveng[gram] = 1
			if gram in sevg:
				sevg[gram] += 1
			else:
				sevg[gram] = 1
	# to find three grams
	# z= len(seveng)
	# ak =1
	# ab=1
	for gram in sevg:
		city = gram.split()
		gm = city[0]+" "+city[1]+" "+city[2]+" "+city[3]+" "+city[4]
		if gm in fiveg:
			fiveg[gm] += sevg[gram]
		else:
			fiveg[gm] = sevg[gram]
		#ab= ab +1
	city = garam.split()	
	for j in range(2):
		gm = city[j+1]+" "+city[j+2]+" "+city[j+3]+" "+city[j+4]+" "+city[j+5]
		if gm in fiveg:
			fiveg[gm] += 1
		else:
			fiveg[gm] = 1
	
	for gram in sevg:
		flag = gram.split()
		gm = flag[0]+" "+flag[1]+" "+flag[2]
		if gm in threeg:
			threeg[gm] += sevg[gram]
		else:
			threeg[gm] = sevg[gram]
	#ak= ak +1
	#flag = garam.split()	
	for x in range(4):
		gm = city[x+1]+" "+city[x+2]+" "+city[x+3]
		if gm in threeg:
			threeg[gm] += 1
		else:
			threeg[gm] = 1

testg={}
traing={}
attacks=["Adduser","Hydra_FTP","Hydra_SSH","Java_Meterpreter","Meterpreter","Web_Shell"]
attak=[dict() for j in range(0,8)]
k=0
for j in attacks:
	threeg = {}
	fiveg = {}
	seveng = {}
	s=sys.argv[1:][0]+"/"+j
	for i in range(1,8):
		d=s+"_"+str(i)
		for f in os.listdir(d):
			generator(threeg,fiveg,seveng,d+"/"+f)
	# print len(seveng)
	# print len(threeg)
	if sys.argv[1:][2]=="3":
		attak[k]=threeg
		l=len(threeg)
		threeg=collections.Counter(threeg).most_common(int(l*0.3))
		for gram in threeg:
			traing[gram[0]]=1
	if sys.argv[1:][2]=="5":
		attak[k]=fiveg
		l=len(fiveg)
		fiveg=collections.Counter(fiveg).most_common(int(l*0.3))
		for gram in fiveg:
			traing[gram[0]]=1			
	if sys.argv[1:][2]=="7":
		attak[k]=seveng		
		l=len(seveng)
		if j == "Adduser":
			print l*0.3
		seveng=collections.Counter(seveng).most_common(int(l*0.3))
		for gram in seveng:
			traing[gram[0]]=1
	k=k+1		

normal={}
d="ADFA-LD/Training_Data_Master"
for f in os.listdir(d):
	threeg = {}
	fiveg = {}
	seveng = {}
	generator(threeg,fiveg,seveng,d+"/"+f)
	if sys.argv[1:][2]=="3":
		normal=threeg
		l=len(threeg)
		threeg=collections.Counter(threeg).most_common(int(l*0.3))
		for gram in threeg:
			traing[gram[0]]=1
	if sys.argv[1:][2]=="5":
		normal=fiveg
		l=len(fiveg)
		fiveg=collections.Counter(fiveg).most_common(int(l*0.3))
		for gram in fiveg:
			traing[gram[0]]=1			
	if sys.argv[1:][2]=="7":
		normal=seveng		
		l=len(seveng)
		seveng=collections.Counter(seveng).most_common(int(l*0.3))
		for gram in seveng:
			traing[gram[0]]=1	

file=open(sys.argv[1:][1]+"_"+str(sys.argv[1:][2]),"w")
for i in range(6):
	testg=attak[i]
	
	file.write(attacks[i]+"\n")
	for gram in traing:
		if gram in testg:
			file.write(str(testg[gram])+"\t\t"+gram+"\n")
		else:
			file.write("0\t\t"+gram+"\n")
testg=normal
file.write("normal\n")
for gram in traing:
	if gram in testg:
		file.write(str(testg[gram])+"\t\t"+gram+"\n")
	else:
		file.write("0\t\t"+gram+"\n")
					
file.close()				