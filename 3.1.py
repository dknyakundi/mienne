hrs=input('Enter hours')
h=float(hrs)
rate=input('Enter rate per hour')
r=float(rate)
if h<=40 :
    gp=h*r
    print(gp)
else :
    gp=(40*r)+((h-40)*(r*1.5))
    print(gp)
    
