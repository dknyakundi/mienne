text = "X-DSPAM-Confidence:    0.8475"
atpos=text.find('0')
spos=text.find('5',atpos)
number=text[atpos:spos+1]
final=float(number)
print(final)
