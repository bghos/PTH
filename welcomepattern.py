import sys

inp = sys.stdin.readline()
N, M = map(int, inp.strip().split())

for i in range(N):
        if i < (N+1)/2 - 1 :
            print('-'*(int((M)/2)-1- 3*i) + '.|.'*(2*i+1) +'-'*(int((M)/2)-1 - 3*i))
        elif i == (N+1)/2 - 1:
            print('-'*int((M-7)/2)+ 'WELCOME'+'-'*int((M-7)/2))
        elif i > (N+1)/2 - 1:
            print('-'*((i - int(N/2))*3) + '.|.'*(2*N-2*i-1) +'-'*((i - int(N/2))*3))
print([i for i in range(1, M+1)])