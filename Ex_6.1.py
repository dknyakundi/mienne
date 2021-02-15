def computepay(a, b):
    if a<=40 :
        gp = (a*b)
        return gp
    else :
        gp=((40*b)+((a-40)*(b*1.5)))
        return gp

Hours=input('Enter hours')
a=float(Hours)
Rate=input('Enter rate per hour')
b=float(Rate)

gp=computepay(a, b)
print("Pay", gp)
