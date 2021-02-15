fname=input('Enter file name')
fopened=open(fname,'r')
lst=list()
for line in fopened:
    words=fopened.split(' ')
    if word in words :
        while False :
            lst.append(word)

lst.sort()
print(lst)
