# brute force solution
arr = [0,3,4,7,9,10]
arr.sort()
cows = 4
def can_we_place(arr,dist,cows):
    countcows = 1
    lastcow = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-lastcow>=dist:
            countcows += 1
            lastcow = arr[i]
        if countcows>=cows:
            return True
    return False
def aggresive_cows(arr,cows):
    for i in range(1,max(arr)-min(arr)+1):
        if (can_we_place(arr,i,cows)):
            continue
        else:
            return i-1
print(aggresive_cows(arr,cows))
# optimal solution
arr = [0,3,4,7,9,10]
cows = 4
def can_we_place(arr,dist,cows):
    countcows = 1
    lastcow = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-lastcow>=dist:
            countcows += 1
            lastcow = arr[i]
        if countcows>=cows:
            return True
    return False
def aggresive_cows(arr,cows):
    arr.sort()
    low = 0
    n = len(arr)
    high = arr[n-1]-arr[0]
    while low<=high:
        mid = (low+high)//2
        if can_we_place(arr,mid,cows):
            low = mid+1
        else:
            high = mid-1
    return high
print(aggresive_cows(arr,cows))