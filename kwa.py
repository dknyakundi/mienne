fname = input("Enter file name: ")
fh = open(fname)
count=dict()

for line in fh:
    if line.startswith("From "):
        email = line.split()[1]
      
        count[email] = count.get(email, 0) + 1
Keymax = max(count, key=count.get)

print(Keymax, count[Keymax])

       


