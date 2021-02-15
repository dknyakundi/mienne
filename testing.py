words=[]
for word in open('romeo.txt').read().split():
    if word not in words:
        words.append(word)
        words.sort()
print(words)
