#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stri = str(number)
last = stri[-1:]
laststri = str(last)
intl = int(last)

# less 6 and not 0
if intl<6 and intl!=0:
    text = "Last digit of "+ stri +" is "+ laststri +" and is less than 6 and not 0"
    print(text)
# greater of 5
if intl>5:
    text = "Last digit of "+ stri +" is "+ laststri +" and is greater than 5"
    print(text)
# if is 0
if intl==0:
    text = "Last digit of "+ stri +" is "+ laststri +" and is 0"
    print(text)
