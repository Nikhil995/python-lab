def neon(n):
    b=n
    s=0
    a=n**2
    while a!=0:
        r=a%10
        s=s+r
        a=a//10
    if(s==n):
        print("neon no")
    else:
        print("not")
n=int(input())
neon(n)
    
