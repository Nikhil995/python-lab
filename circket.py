'''program to input the no of overs in a circket match and output the maximum runs a player can score in the match. Assume that there are no extra runs or NO balls in the match played.
For example, in a 50 over match, the maximum runs scored are 1653.'''
a=int(input("enter no of overs"))
m=5*(a-1)*6+(a-1)*3+36
print("the maximum runs scored are ",format(m))
