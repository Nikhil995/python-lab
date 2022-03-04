''' there is a men has certain amount of apple,if he make group of 7-7  sets then at last no apple was left  but when he make group of 6,5,4,3,2 then 1 apple is left.Find minimum number of
apples then there is no apple is left. ans-301'''
a=int(input("enter the minimum no of apple"))
if(a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1 and a%2==1):
    print("yes that is minimum required no of apples")
else:
    print("no")
