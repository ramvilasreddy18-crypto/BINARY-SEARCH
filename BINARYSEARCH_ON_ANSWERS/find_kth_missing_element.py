# brute force solution 
arr = [2,3,4,7,11]
k = 5
n = len(arr)
for i in range(n):
    if arr[i]<=k:
        k += 1
    else:
        break
print(k)
# optimal solution
arr = [2,3,4,7,11]
k = 5
n = len(arr)
def missing(arr,k,n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        missing = arr[mid]-(mid+1)
        if missing < k:
            low = mid+1
        else:
            high = mid-1
    return low+k
print(missing(arr,k,n))