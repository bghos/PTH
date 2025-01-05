import sys
import numpy as np

''' Task

You are given a square matrix  with dimensions X. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer .
The next  lines contains the  space separated elements of array .

Output Format

Print the determinant of . '''

print('-------------------------')
counter:int = 0
N: int = 0
matrices = []

Ntest:str = sys.stdin.read(1)
N = int(Ntest)

# print(N)


for _ in range(N+1):
    line = sys.stdin.readline().strip()  
    counter =+ 1
    # print("matrics: ", matrices)
    row = list(map(float, line.split()))
    if len(row) > 0 :
        matrices.append(row)


print('------------Output-------------')

matricarray = np.array(matrices)
matrixnxn = matricarray.reshape(N,N)

determinant = np.linalg.det(matrixnxn)
print(determinant)




