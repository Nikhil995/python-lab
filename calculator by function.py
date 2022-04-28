def cal(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    return l
x=int(input())
y=int(input())
print(cal(x,y))
