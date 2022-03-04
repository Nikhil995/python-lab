# 3program to  enter 3 sides of a triangle and check it is valid or not.
a=int(input("enter the 1st side"))
b=int(input("enter the 2nd side"))
c=int(input("enter the 3rd side"))
if(a<b+c or b<a+c or c<a+b):
    print("triangle is valid")
else:
    print("triangle is not valid")
