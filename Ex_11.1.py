import re

hand=open('11.0.txt')
x=list()
for line in hand:
    num = re.findall('[0-9]+' ,line)
    x=(x+num)
    
sum=0
for n in x:
    sum=sum+int(n)

print(sum)