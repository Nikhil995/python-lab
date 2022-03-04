'''write a program to generaye sallery of an employee when the conditions are-
1. if the basic sallary is less than 10000 then HRA(house rent anounce) will be 80% of basic sallary and DA(daily anounce) will be 90% of basic sallery.
2. if the basic sallery  is greater then 10000 and less then 20000 then HRA is 85% of basic sallery and DA will be 90% of his basic sallery.
3. if basic sallery > 20000 then DSA will be 95% and DA will be 95%.
then calculate sallery of an employee.'''
a=int(input("enter the basic sallery of employee"))
if(a<10000):
    b=a+0.8*a+0.9*a
    print("sallery of employee is",format(b))
elif(a>10000 and a<=20000):
    b=a+0.85*a+0.90*a
    print("sallery of employee is",format(b))
elif(a>20000):
    b=a+ 0.95*a+0.95*a
    print("sallery of employee is",format(b))
