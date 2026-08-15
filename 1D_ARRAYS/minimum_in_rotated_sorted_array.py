# brute force smallest ele in array
arr = [4,5,6,7,0,1,2]
n = len(arr)
ans = float('inf')
for i in range(n):
    if ans>arr[i]:
        ans = arr[i]
print(ans)
# optimal solution using binary search
arr = [4,5,6,7,0,1,2]
n = len(arr)
def minimum_rotated(arr,n):
    low = 0
    high = n-1
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2
        if arr[low]<=arr[mid]:
            ans = min(ans,arr[low])
            low = mid+1
        else:
            ans = min(ans,arr[mid])
            high = mid-1
    return ans
print(minimum_rotated(arr,n))
# more optimization
arr = [4,5,6,7,0,1,2]
n = len(arr)
def minimum_rotated(arr,n):
    low = 0
    high = n-1
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2
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
