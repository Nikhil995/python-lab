# program to reverse a number.
n=int(input())
s=0
while n:
    r=n%10
    s=s*10+r
    n=n//10
print(s)
