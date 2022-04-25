'''{1:0,2:1,3:1,4:2,5:3,6:5........}'''
d={}
n=int(input("no of terms"))
d[1]=0
d[2]=1
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
print(d)
    
