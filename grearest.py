#program to find greatest  of 3 numbers
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter the 3rd no"))
if(a>b and a>c):
    print("a is grearest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")
