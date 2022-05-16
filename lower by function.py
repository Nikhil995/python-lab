#program to convert string into lowercase.
def lower(s):
    a=''
    for i in s:
        a=a+chr(ord(i)+32)
    print(a)
s=input()
lower(s)
