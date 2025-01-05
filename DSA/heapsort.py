

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
    


def heapSort(arr):
    n=len(arr)
    # Build a maxheap.
    # Since last parent will be at (n//2) we can start at that location.
    print("n//2-1:",n//2-1)
    print("-----------------")
    for i in range(n//2-1,-1,-1):
        print(arr," ",n," ",i)
        heapify(arr,n,i)
    print("-----------------")
    for i in range(n-1,0,-1):
        print(f"arr[{i}],arr[0]:",arr[i],arr[0])
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    print("-----------------")
    print(arr)
    

arr = [12, 11, 13, 5, 6, 4, 8]
heapSort(arr)