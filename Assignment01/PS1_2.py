import numpy as np

# question 2.1
M1=np.random.randint(0, 51, size=(5, 10))
M2=np.random.randint(0, 51, size=(10, 5))

print('M1\n',M1)
print('M2\n',M2)

# question 2.2
def Matrix_multip(M1,M2):
    Result=np.zeros((M1.shape[0],M2.shape[1]))
    for i in range(Result.shape[0]):
        for j in range(Result.shape[1]):
            for k in range(M1.shape[1]):
                Result[i,j]+=M1[i,k]*M2[k,j]
    return Result


print('M1M2\n',Matrix_multip(M1,M2))