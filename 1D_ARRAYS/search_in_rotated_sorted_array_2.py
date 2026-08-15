arr = [3,1,2,3,3,3,3]
n = len(arr)
target = 3
def search_rotated(arr,n,target):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return True
        if arr[mid] == arr[low] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low]<=arr[mid]:
            if arr[low]<=target<=arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=target<=arr[high]:
                low = mid+1
            else:
                high = mid-1
    return False
print(search_rotated(arr,n,target))
