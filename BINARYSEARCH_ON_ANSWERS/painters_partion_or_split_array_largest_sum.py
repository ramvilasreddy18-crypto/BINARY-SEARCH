arr = [10,20,30,40]
k = 2
def partion(arr,paint):
    painters =1
    units = 0
    for i in range(len(arr)):
        if units+arr[i]>paint:
            painters += 1
            units = arr[i]
        else:
            units += arr[i]
    return painters
def painters(arr,k):
    low = max(arr)
    high = sum(arr)
    while low<=high:
        mid = (low+high)//2
        painters = partion(arr,mid)
        if painters>k:
            low = mid+1
        else:
            high = mid-1
    return low
print(painters(arr,k))