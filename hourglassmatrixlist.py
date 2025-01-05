

def hourglassSum(arr):
    sum = 0
    maxsum = -100
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum > maxsum:
                maxsum = sum
    return maxsum


arr = []
for _ in range(6):
    arr1 = []
    arr1 = list(map(int,input().strip().split()))
    arr.append(arr1)
# print(arr)

result = hourglassSum(arr)
print(result)
    
