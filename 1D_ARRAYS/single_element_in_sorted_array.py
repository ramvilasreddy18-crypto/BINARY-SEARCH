# brute force solution
arr = [1,1,2,2,3,3,4,5,5,6,6]
n = len(arr)
def single_element(arr,n):
    for i in range(n):
        if i == 0 :
            if arr[i] != arr[i+1]:
                return arr[i]
        elif i == n-1:
            if arr[i] != arr[i-1]:
                return arr[i]
        else:
            if (arr[i]!=arr[i+1] and arr[i]!=arr[i-1]):
                return arr[i]
    return -1
print(single_element(arr,n))
# optimal solution using binary search
arr = [1,1,2,2,3,3,4,5,5,6,6]
n = len(arr)
def single_element(arr,n):
    if n == 1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    low = 1
    high = n-2
    while low<=high:
        mid = (low+high)//2
        if arr[mid]!= arr[mid+1] and arr[mid]!=arr[mid-1]:
            return arr[mid]
        # we are in left half
        if ((mid%2 == 1 and arr[mid]==arr[mid-1]) or (mid%2 == 0 and arr[mid] == arr[mid+1]) ):
            low = mid+1
        else:
            high = mid-1
    return -1
print(single_element(arr,n))
