n=int(input())
i=1
j=1
while(i<=n):
    while(j<=i):
        print("*"*i,end="")
        j=j+1
    print(" ")
    i=i+1
