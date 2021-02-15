fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    wrds=line.split()
    for word in wrds:
        if word not in words:
            lst.append(word)
lst.sort()
print(lst)
