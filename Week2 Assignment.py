import re
fname=open('input.txt')
numlist=list()
so=0
for line in fname:
    line=line.strip()
    struff=re.findall('[0-9]+',line)
    if len(struff)<= 0 : continue
    for num in  struff:
        numlist.append(int(num))
so=sum(numlist)
print (so)
