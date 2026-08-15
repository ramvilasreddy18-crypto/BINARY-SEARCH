arr = [4,5,6,7,0,1,1,1,1,1,2,2,2,2]
n = len(arr)
def minimum_rotated(arr,n):
    low = 0
    high = n-1
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low]<=arr[high]:
            ans = min(ans,arr[low])
            break
        if arr[low]<=arr[mid]:
            ans = min(ans,arr[low])
            low = mid+1
        else:
            ans = min(ans,arr[mid])
            high = mid-1
    return ans
print(minimum_rotated(arr,n))
