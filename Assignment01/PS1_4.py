import random

def Least_moves(x):
    if(x==1):
        return 0
    elif(x%2!=0):
        return 1+Least_moves(x-1)
    else:
        return 1+min(Least_moves(x-1),Least_moves(int(x/2)))
    
x=random.randint(0,101)
print('x=',x)
print('Least moves=',Least_moves(x))