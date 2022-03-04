# to find compound intre
p=int(input("enter the principle amount"))
r=float(input("enter the intrest rate"))
t=int(input("enter the time"))
ci=(p*((1+r/100)**t)-p)
print("compound intrest=",ci)
