count=0
apos=0
fname=input('Enter the file name: ')
ofile=open(fname,'r')
for line in ofile :
    if line.startswith ('X-DSPAM-Confidence:') :
        count=count+1
        atpos=line.find('0')
        spos=line[atpos:atpos+6]
        apos=float(spos)+apos

avg=apos/count
print('Average spam Confidence: ', avg)
