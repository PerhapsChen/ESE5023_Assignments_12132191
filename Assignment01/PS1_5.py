import numpy as np
import random
import matplotlib.pyplot as plt

def Find_expression(x,print_str=True):
    string_0='a1b2c3d4e5f6g7h8i9'
    all_str=[]
    w=['+','-','']
    for a in ['-','']:
        for b in w:
            for c in w:
                for d in w:
                    for e in w:
                        for f in w:
                            for g in w:
                                for h in w:
                                    for i in w:
                                        str_t=string_0.replace('a',a)
                                        str_t=str_t.replace('b',b)
                                        str_t=str_t.replace('c',c)
                                        str_t=str_t.replace('d',d)
                                        str_t=str_t.replace('e',e)
                                        str_t=str_t.replace('f',f)
                                        str_t=str_t.replace('g',g)
                                        str_t=str_t.replace('h',h)
                                        str_t=str_t.replace('i',i)
                                        all_str.append(str_t)
    cnt=0
    for i in range(len(all_str)):
        if(count_str(all_str[i])==x):
            if(print_str==True):
                print(all_str[i],'=',x)
            else:
                pass
            cnt+=1
    return cnt

def count_str(string):
    string+='e'
    i=0
    result=0
    num='0'
    t='+'
    while(string[i]!='e'):
        if(string[i] not in ['+','-']):
            num+=string[i]
        elif(string[i]=='+'):
            if(t=='+'):
                result+=int(num)
            else:
                result-=int(num)
            t='+'
            num='0'
        elif(string[i]=='-'):
            if(t=='+'):
                result+=int(num)
            else:
                result-=int(num)
            t='-'
            num='0'
        i+=1
    if(t=='+'):
        result+=int(num)
    else:
        result-=int(num)
    return result

x=random.randint(0,101)
print('x=',x,'\n we can find the expression:')
solu_num=Find_expression(x)
print('the number of solutions for',x,'is',solu_num)

x=np.arange(0,101)
y=[]

for i in range(len(x)):
    y.append(Find_expression(x[i],print_str=False))
    
fig,ax=plt.subplots()
ax.plot(x,y,label='a')
plt.xlabel('the given sum x')
plt.ylabel('the number of solutions')

max_solutions=max(y)
min_solutions=min(y)
max_index=y.index(max_solutions)
min_index=y.index(min_solutions)
print('the max number of solutions is',max_solutions)
print('the max number of solutions is yield by the number:',max_index)
print('the min number of solutions is',min_solutions)
print('the min number of solutions is yield by the number:',min_index)