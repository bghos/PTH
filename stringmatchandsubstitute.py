'''.git\ask

You are given a text of  lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format

The first line contains the integer, .
The next  lines each contain a line of the text.

Constraints


Neither && nor || occur in the start or end of each line.

Output Format

Output the modified text.'''


import re

def modify_text(n, text):
    for i in range(n):
        # text[i] = text[i].replace(' && ', ' and ').replace(' || ', ' or ')
        text[i] = re.sub(r'(?<= )&&(?= )', 'and', text[i])
        text[i] = re.sub(r'(?<= )\|\|(?= )', 'or', text[i])

    return text

if __name__ == '__main__':
    n = int(input())
    text = [input() for i in range(n)]
    print(*modify_text(n, text), sep='\n')