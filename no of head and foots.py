#program to input the no of heads and feets  in a farm and identify the no of chikens and goats in the farm. for example, if there are 340 heads and 1060 feets,there are 150 chikens and 190 goats.
a=int(input("enter no of heads"))
b=int(input("enter no of feets"))
c=((4*a)-b)/2
h=a-c
print("there are {0} chikens and{1} goats".format(c,h)) 
 
