#!/usr/bin/python3.5
import sys
import collections
fra=eng=deu=0.0
en=collections.defaultdict(float)
fr=collections.defaultdict(float)
de=collections.defaultdict(float)
for i in open(sys.argv[1],'r').read().splitlines():
    en[i.split(sep='\t')[0]]=float(i.split('\t')[1])

for i in open(sys.argv[2],'r').read().splitlines():
    fr[i.split(sep='\t')[0]]=float(i.split('\t')[1])

for i in open(sys.argv[3],'r').read().splitlines():
    de[i.split(sep='\t')[0]]=float(i.split('\t')[1])

with open(sys.argv[4]) as f:
    for i in f:
        str=i.lower()
        for j in range(len(str)-2):
            if str[j:j+3] in en.keys():
                eng+=1
            if str[j:j + 3] in fr.keys():
                fra += 1
            if str[j:j + 3] in de.keys():
                deu += 1

m=max(fra,eng,deu)
#print(m,fra,eng,deu)
if m==fra:
    print("French")
elif m==eng:
    print("English")
else:
    print("German")
