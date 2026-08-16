# brute force solution
arr = [1,2,3,4,5,6,7,8,5,1]
n = len(arr)
def peak_element(arr,n):
    for i in range(n):
        if ((i==0) or arr[i-1] < arr[i]) and ((i == n-1) or arr[i] > arr[i+1]):
            return i  
    return -1
print(peak_element(arr,n))
# optimal solution 
arr = [1,2,3,4,5,6,7,8,5,1]
n = len(arr)
def peak_element(arr,n):
    if n == 1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low = 1
    high = n-2
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low = mid+1
        else:
            high = mid-1
    return -1
print(peak_element(arr,n))
