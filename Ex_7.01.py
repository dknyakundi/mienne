fname=input('Enter the file name: ')
fhand=open(fname)
fread=fhand.read()
rdent=fread.rstrip()
final=rdent.upper()
print(final)
