# brute force solution
x = 10
arr = [2,4,6,8,8,11,13]
n = len(arr)
first = -1
last = -1
for i in range(n):
    if arr[i] == x:
        if first == -1:
            first = i
        last = i
print([first,last])
#  optimal solution
k = 8
arr = [2,4,6,8,8,11,13]
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
def first_last(arr,k,n):
    lb = lower_bound(arr,k,n)
    if lb == n or arr[lb] != k:
        return (-1,-1)
    return {lb,upper_bound(arr,k,n)}
print(first_last(arr,k,n))
# optimal solution without lb and upb
x = 8
arr = [2,4,6,8,8,11,13]
n = len(arr)
def first_occurance(arr,n,x):
    low = 0
    high = n-1
    first = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == x:
            first = mid
            high = mid-1
        elif arr[mid]>x:
            high = mid-1
        else:
            low = mid+1
    return first
def last_occurance(arr,n,x):
    low = 0
    high = n-1
    last = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == x:
            last = mid
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
        else:
            low = mid+1
    return last
def first_last(arr,n,x):
    first = first_occurance(arr,x,n)
    if first == -1:
        return [-1,-1]
    last = last_occurance(arr,x,n)
    return {first,last}
print(first_last(arr,x,n))
