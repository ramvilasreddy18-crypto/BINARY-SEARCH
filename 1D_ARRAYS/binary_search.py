# Iterative code
arr = [3,4,6,7,9,12,16,17]
n = len(arr)
target = 13
def binary_search(arr,n,target):
    low = 0
    high = n-1
    while (low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1
print(binary_search(arr,n,target))
# recursive code
arr = [3,4,6,7,9,12,16,17]
n = len(arr)
target = 13
def bs(arr,low,high,target):
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        return bs(arr,low,mid-1,target)
    return bs(arr,mid+1,high,target)
print(bs(arr,0,n-1,target))
