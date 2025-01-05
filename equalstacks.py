'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

Example

There are  and  cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from  (heights = [1, 2]) and from  (heights = [1, 1]) so that the three stacks all are 2 units tall. Return  as the answer.
Note: An empty stack is still a stack.
Function Description
Complete the equalStacks function in the editor below.
equalStacks has the following parameters:
int h1[n1]: the first array of heights
int h2[n2]: the second array of heights
int h3[n3]: the third array of heights
Returns
int: the height of the stacks when they are equalized
Input Format
The first line contains three space-separated integers, , , and , the numbers of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:
The second line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
The third line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
The fourth line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
'''

def equalStacks(h1, h2, h3):
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)

    # Initialize pointers for each stack
    i1 = i2 = i3 = 0

    # Loop until one of the stacks is empty
    while i1 < len(h1) and i2 < len(h2) and i3 < len(h3):
        # Find the minimum sum of the three stacks
        min_sum = min(sum_h1, sum_h2, sum_h3)

        # Adjust the sums and pointers to make them equal
        while sum_h1 > min_sum:
            sum_h1 -= h1[i1]
            i1 += 1
        while sum_h2 > min_sum:
            sum_h2 -= h2[i2]
            i2 += 1
        while sum_h3 > min_sum:
            sum_h3 -= h3[i3]
            i3 += 1

        # Check if all sums are equal
        if sum_h1 == sum_h2 == sum_h3:
            return sum_h1

    # If no equal height is found, return 0
    return 0


first_multiple_input = input().rstrip().split()
n1 = int(first_multiple_input[0])
n2 = int(first_multiple_input[1])
n3 = int(first_multiple_input[2])
h1 = list(map(int, input().rstrip().split()))
h2 = list(map(int, input().rstrip().split()))
h3 = list(map(int, input().rstrip().split()))
result = equalStacks(h1, h2, h3)
print(result)