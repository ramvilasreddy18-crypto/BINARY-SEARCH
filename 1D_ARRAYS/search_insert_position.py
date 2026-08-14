# same algo as lower bound
arr = [1,2,4,7]
x = 6
n = len(arr)
def search_insert_position(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
print(search_insert_position(arr,n,x))
