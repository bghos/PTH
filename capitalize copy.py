import os

def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    
    return s
    # return s.title() # this is the same as the above code but with a minor \
    # difference it looks for first avaulable character and capitalizes it
    # instead of capitalizing the first character of each word 

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    # print(result)

    fptr.write(result + '\n')

    fptr.close()
