largest=None
smallest=None
while True :
    num=input('Enter an integer number: ')
    if num =='done' :
        break
    try:
        no=int(num)
    except:
        print('Invalid input')
        continue

#to find the smallest value

    for value in [no] :
        if smallest is None :
            smallest=value
        elif value<smallest :
            smallest=value

#to find the largest value

    for value in [no] :
        if largest is None :
            largest=value
        elif value>largest :
            largest=value

print('Maximum is', largest)
print('Minimum is', smallest)
