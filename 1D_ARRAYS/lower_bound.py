# lower bound 
arr = [1,2,3,3,5,8,8,10,10,11]
x = 12
n = len(arr)
def lower_bound(arr,x,n):
    ans = n # hypothetical answer
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
print(lower_bound(arr,x,n))


