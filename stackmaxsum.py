'''Alexa has two stacks of non-negative integers, stack  and stack  where index  denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack  or stack .
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer  given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given , , and  for  games, find the maximum possible score Nick can achieve.

Example


The maximum number of values Nick can remove is . There are two sets of choices with this result.

Remove  from  with a sum of .
Remove  from  and  from  with a sum of .
Function Description
Complete the twoStacks function in the editor below.

twoStacks has the following parameters: - int maxSum: the maximum allowed sum
- int a[n]: the first stack
- int b[m]: the second stack

Returns
- int: the maximum number of selections Nick can make

Input Format

The first line contains an integer,  (the number of games). The  subsequent lines describe each game in the following format:

The first line contains three space-separated integers describing the respective values of  (the number of integers in stack ),  (the number of integers in stack ), and  (the number that the sum of the integers removed from the two stacks cannot exceed).
The second line contains  space-separated integers, the respective values of .
The third line contains  space-separated integers, the respective values of .
Constraints

Subtasks

 for  of the maximum score.'''


def twoStacks(maxSum, a, b):
    # Write your code here
    n = len(a)
    m = len(b)
    sum = 0
    count = 0
    i = 0
    j = 0
    while i < n and sum + a[i] <= maxSum:
        sum += a[i]
        i += 1
        count += 1
    result = count
    while j < m and i >= 0:
        sum += b[j]
        j += 1
        while sum > maxSum and i > 0:
            i -= 1
            sum -= a[i]
        if sum <= maxSum and i + j > result:
            result = i + j
    return result



g = int(input().strip())

for g_itr in range(g):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        maxSum = int(first_multiple_input[2])
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = twoStacks(maxSum, a, b)
        print(result)