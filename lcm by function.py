#wap using function to find lcm of two no.
def lcm(a,b):
    if a<b:
        s=a
    else:
        s=b
    for i in range(1,s+1):
        if((a%i==0) and(b%i==0)):
            hcf=i
    print((a*b)//hcf)
a=int(input())
b=int(input())
lcm(a,b)
