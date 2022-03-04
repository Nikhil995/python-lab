'''write a program to input electricity charge and calculate electricity bill according to the following conditions-
1. for first 50 units Rs 50 paise per unit.
2. for next 100 units Rs 75 paise per unit.
3. for next 100 units Rs 1.20 per unit.
4. for above 250 units Rs 1.50 per units.'''
a=int(input("enter no of units"))
x=a-50
y=a-150
z=a-250 
if(a<=50):
    b=a*.50
    print("amount of bill is",format(b))
elif(a>50 and a<=150):
    x=a-50
    b=50*.50+x*.75
    print("amount of bill is",format(b))
elif(a>150 and a<=250):
    y=a-150
    b=50*.50+100*.75+y*1.20
    print("amount of bill is",format(b))
elif(a>250):
    z=a-250 
    b=50*.50+100*.75+100*1.20+z*1.50
    print("amount of bill is",format(b))
