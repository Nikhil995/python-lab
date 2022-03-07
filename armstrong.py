# program to check wheather the no is armstrong or not
n=int(input())
s=0
a=n
b=n
c=0
while n>0:
    c=c+1
    n=n//10
while a:
    r=a%10
    s=s+r**c
    a=a//10
if s==b:
    print("armstrong no")
else:
    print("not armstromg")
