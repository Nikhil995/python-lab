# program to print the armstrong no  between 1 to n
n=int(input())
i=10
while i<=n:
    s=0
    a=i
    b=i
    k=i
    c=0
    while k:
        c=c+1
        k=k//10
    while a:
        r=a%10
        s=s+r**c
        a=a//10
    if s==b:
        print(s)
    i=i+1

