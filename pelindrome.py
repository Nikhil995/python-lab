#program to check wheather the no is pelindrome or not
n=int(input())
a=n
s=0
while n:
    r=n%10
    s=s*10+r
    n=n//10
if s==a:
    print("pelindrome")
else:
    print("not pelindrome")
