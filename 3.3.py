s=input('Enter Score: ')
sc=float(s)
if sc>1.0 or sc<0.0 :
    print('Score out of Range!')
    quit()
elif sc>=0.9 :
    print('A')
elif sc>=0.8 :
    print('B')
elif sc>=0.7 :
    print('C')
elif sc>=0.6 :
    print('D')
else :
    print('F')
