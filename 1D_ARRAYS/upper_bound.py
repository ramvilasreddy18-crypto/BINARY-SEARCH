# upper bound 
arr = [2,3,6,7,8,8,11,11,11,12]
x = 11
n = len(arr)
def upper_bound(arr,x,n):
    low = 0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2
        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
print(upper_bound(arr,x,n))
