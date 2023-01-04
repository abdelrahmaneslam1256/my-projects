import random
i=0
p=0

while True:
    x=input("s or r or p? ")
    if x==1:
        x = 'r'
    elif x== 2:
        x = 's'
    else :
        x ='p'
    l= random.randint(1,3)
    if l==1:
        y='r'
    elif l== 2:
        y='s'
    else:
        y='p'
    z=x
    if z == y:
        print("again t3adoll")
    elif z== 's' and y == 'p' :
        i=i+1
    elif z== 'r' and y == 's'  :
        i=i+1
    elif z== 'p' and y == 'r' :
        i=i+1
    elif y== 's' and z == 'p' :
        p=p+1
    elif y== 'r' and z == 's' :
        p=p+1
    elif y== 'p' and z == 'r' :
        p=p+1
    print ("p1 ",i," p2 ",p," times")