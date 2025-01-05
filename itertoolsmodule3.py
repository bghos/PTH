'''

You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and .
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

Constraints

Output Format

Output a single integer denoting the value .'''
from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
# print("N= ",N)
results = list(map(lambda x: sum(i**2 for i in x) % M, product(*N)))
# print("results:", results)
print(max(results))