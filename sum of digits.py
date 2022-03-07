# program to take a no and find the sum of its digits.
n=int(input())
s=0
while n:
    r=n%10
    s=s+r
    n=n//10
print(s)

