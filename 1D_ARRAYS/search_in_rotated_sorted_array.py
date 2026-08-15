# brute force linear search 
# arr = [4,5,6,7,0,1,2]
# n = len(arr)
# target = 0
# for i in range(n):
#     if arr[i] == target:
#         print(i)
#         break
# optimal solution using binary search
arr = [4,5,6,7,0,1,2]
n = len(arr)
target = 0
def sirsa(arr,n,target):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[low]<=arr[mid]:
            if arr[low]<=target<=arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=target<=arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1
print(sirsa(arr,n,target))
