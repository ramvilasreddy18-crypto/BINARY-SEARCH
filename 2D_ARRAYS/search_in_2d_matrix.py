# brute force
# linear search time complexity = O(n*m)
# optimal solution
arr = [[10,20,30,40],
       [11,21,36,43],
       [25,29,39,50],
       [50,60,70,80]]
target = 60
def search_ele_in_2d(arr,x): 
    n = len(arr)
    m = len(arr[0])
    i = 0
    j = m-1
    while (i<n and j>=0):
        if (arr[i][j]==x):
            return True
        if (arr[i][j]>x):
            j -= 1
        else:
            i += 1
    return False
print(search_ele_in_2d(arr,target))
# leetcode optimal solution
arr = [[10,20,30,40],
       [11,21,36,43],
       [25,29,39,50],
       [50,60,70,80]]
target = 60
def search_ele_in_2d(arr,x):
    if len(arr) == 0:
        return False
    n = len(arr)
    m = len(arr[0])
    low = 0
    high = n*m-1
    while low<=high:
        mid = (low+high)//2
        value = arr[mid//m][mid%m]
        if x == value:
            return True
        if value<x:
            low = mid+1
        else:
            high = mid-1
    return False
print(search_ele_in_2d(arr,target))