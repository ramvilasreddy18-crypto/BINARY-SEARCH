arr = [3,4,5,1,2]
n = len(arr)
def number_rotated(arr,n):
    ans = float('inf')
    index = -1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[low]<=arr[high]:
            if arr[low]<ans:
                index = low
                ans = arr[low]
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                index = low
                ans = arr[low]
            low = mid+1
        else:
            high = mid-1
            if arr[mid]<ans:
                index = mid
                ans = arr[mid]
    return index
print(number_rotated(arr,n))
            