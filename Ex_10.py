fname = input("Enter file name: ")
fh = open(fname)
count=dict()

for line in fh:
    if line.startswith("From "):
        time= line.split()[5]
        hour=time.split(':')[0]
        count[hour] = count.get(hour, 0) + 1
for (k,v) in sorted(count.items()):
    print(k,v)




