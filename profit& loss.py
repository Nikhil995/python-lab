# program to calculate profit & loss percent.
sp=int(input("enter the selling price"))
cp=int(input("enter the cost price"))
if(cp>sp):
    l=((cp-sp)/sp)*100
    print("loss percentage is",format(l))
else:
    p=((sp-cp)/cp)*100
    print("profit percentage is",format(p))
             
