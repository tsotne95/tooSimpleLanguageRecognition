#!/usr/bin/python3.5
import sys
import collections
c=0
en=collections.defaultdict(int)
with open(sys.argv[1]) as f:
    for i in f:
        str=i.lower().strip();
        for j in range(len(str)-2):
            c+=1
            en[str[j:j+3]]+=1

for i,j in en.items():
    print(i,j/c*100,sep='\t')
