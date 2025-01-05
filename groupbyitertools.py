'''You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input'''
from itertools import groupby
s: str = input()
for k,g in groupby(s):
    # print(k,g)
    print((len(list(g)),int(k)),end=' ')