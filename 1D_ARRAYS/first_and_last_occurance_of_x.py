# brute force solution
# x = 10
# arr = [2,4,6,8,8,11,13]
# n = len(arr)
# first = -1
# last = -1
# for i in range(n):
#     if arr[i] == x:
#         if first == -1:
#             first = i
#         last = i
# print([first,last])
# # optimal solution
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