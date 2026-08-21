# brute force solution
arr = [[0,0,1,1,1],
       [0,0,0,0,0],
       [0,1,1,1,1],
       [0,0,0,0,0],
       [0,1,1,1,1]]
max_count = -1
index = -1
n = 5
m = 5
for i in range(n):
    count = 0
    for j in range(m):
        count += arr[i][j]
    if count>max_count:
        max_count = count
        index = i
print(index)
# optimal solution
arr = [[0,0,1,1,1],
       [0,0,0,0,0],
       [0,1,1,1,1],
       [0,0,0,0,0],
       [0,1,1,1,1]]
n = 5
m = 5
def lower_bound(arr,x,n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            high = mid-1
        else:
            low = mid+1
    return low
def row_with_max1_s(arr,n,m):
    count_max = 0
    index = -1
    for i in range(n):
        count_ones = m - lower_bound(arr[i],m,1)
        if count_ones>count_max:
            count_max = count_ones
            index = i
    return index

