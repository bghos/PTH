'''
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings

Returns
- int[]: the answers to each type 3 query '''


import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = []
    max_item = []
    count_max = 0
    for item in operations:
        # print(item)
        item = item.split()
        if item[0] == '1':
            # print('Push the element x into the stack')
            stack.append(int(item[1]))
            print(stack)
        elif item[0] == '2':
            # print('Delete the element present at the top of the stack')
            if stack: 
                stack.pop()
            print(stack)
        elif item[0] == '3':
            # print('Print the maximum element in the stack')
            # print(max(stack))
            if stack:
                count_max += 1
                max_item.append(max(stack))
                print("max called - ", count_max,' - ', max_item)
    return max_item
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ops = []
    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)
    # print(res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    # fptr.close()
