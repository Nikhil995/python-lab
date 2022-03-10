''' enter a phone no then find the sum of its even &odd digits & compare the sum if equal,than the no is magice= otherwise not.'''
n=int(input())
i=1
even=0
odd=0
while(i<=10):
    if(i%2==0):
        r=n%10
        even=even+r
        n=n//10
    else:
        m=n%10
        odd=odd+m
        n=n//10
    i=i+1
if(odd==even):
    print("magic number")
else:
    print("not magic number")
        
