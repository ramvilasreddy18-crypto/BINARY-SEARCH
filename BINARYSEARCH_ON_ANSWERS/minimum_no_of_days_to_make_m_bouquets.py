# brute force solution
arr = [7,7,7,7,13,11,12,7]
m = 2
k = 3
n = len(arr)
def possible(arr,day,m,k):
    count = 0
    no_of_bouq = 0
    for i in range(len(arr)):
        if arr[i]<=day:
            count += 1
        else:
            no_of_bouq += count//k
            count = 0
    no_of_bouq += count//k
    if no_of_bouq>=m:
        return True
    else:
        return False
def bouq(arr,n,m,k):
    if (n<m*k):
        return -1
    for i in range(min(arr),max(arr)+1):
        if (possible(arr,i,m,k)):
            return i
    return -1
print(bouq(arr,n,m,k))
# optimal solution
arr = [7,7,7,7,13,11,12,7]
m = 2
k = 3
n = len(arr)
def possible(arr,day,m,k):
    count = 0
    no_of_bouq = 0
    for i in range(len(arr)):
        if arr[i]<=day:
            count += 1
        else:
            no_of_bouq += count//k
            count = 0
    no_of_bouq += count//k
    if no_of_bouq>=m:
        return True
    else:
        return False
def binary_search(arr,n,m,k):
    if n<m*k:
        return -1
    low = min(arr)
    high = max(arr)
    while low<=high:
        mid = (low+high)//2
        if possible(arr,mid,m,k):
            high = mid-1
        else:
            low = mid+1
    return low
print(binary_search(arr,n,m,k))
