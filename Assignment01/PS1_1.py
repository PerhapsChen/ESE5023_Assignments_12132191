def Print_values(a,b,c):
    if (a>b):
        if(b>c):
            print(a,b,c)
        else:
            if (a>c):
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if(b>c):
            if(a>c):
                print(c,a,b)
        else:
            print(c,b,a)

import random
a=random.randint(0,999)
b=random.randint(0,999)
c=random.randint(0,999)
print('init a,b,c:')
print(a,b,c)
print('\nafter function a,b,c:')
Print_values(a,b,c)