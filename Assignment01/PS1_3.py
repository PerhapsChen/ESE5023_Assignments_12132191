from scipy.special import comb
import numpy as np

def Pascal_triangle(k):
    Result=np.zeros((k))
    for i in range(k):
        Result[i]=comb(k-1,i)
    print(Result)

print('100th line of  the Pascal triangel:')
Pascal_triangle(100)
print('200th line of  the Pascal triangel:')
Pascal_triangle(200)