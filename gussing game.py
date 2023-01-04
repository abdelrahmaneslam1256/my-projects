import random
n= int(random.randrange(1,100))
x = int(input("input num "))
while n!=x : 
    if n<x:
         x=int(input(" high gusse again: "))
    elif n > x :
         x=int(input("low gusse again: "))
         
    else:
         break
print ("correct")         