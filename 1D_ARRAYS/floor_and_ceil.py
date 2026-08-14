# floor = largest no in array <= x and ceil = smallest no in array >= x
arr = [10,20,30,40,50]
n = len(arr)
x = 25
def floor(arr,x,n):
    low = 0
    high = n-1
    floor_ans = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=x:
            floor_ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return floor_ans
def ceil(arr,x,n):
    ceil_ans = -1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ceil_ans = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return ceil_ans
print(ceil(arr,x,n),floor(arr,x,n))