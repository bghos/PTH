'''.given a string and an integer k, split the string into k-sized substrings. Each substring must contain distinct characters. Print each substring on a new line in the same order it appears in the input string.
AABCAAADA
3
AB
CA
AD

'''


def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        sub_string = string[i:i+k]
        unique = ''
        for j in sub_string:
            if j not in unique:
                unique += j
        # unique = ''.join(list(set(sub_string)))
        print(unique)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)