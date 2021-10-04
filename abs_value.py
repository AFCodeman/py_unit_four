import math

def absvalue():
    x = float(input("Assign a value for X. "))
    if x>0:
        print("The absolute value of",x,"is equal to",x*1)
    if x<0:
        print("The absolute value of", x, "is equal to",x*-1)
    if x==0:
        print("The absolute value of 0 is equal to 0")


absvalue()