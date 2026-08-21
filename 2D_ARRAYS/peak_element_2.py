mat = [[4,2,5,1,4,6],
       [2,9,3,2,3,2],
       [1,7,6,0,1,3],
       [3,6,2,3,7,2]]
def find_max_index(mat,n,m,col):
    max_value = -1
    index = -1
    for i in range(n):
        if mat[i][col]>max_value:
            max_value = mat[i][col]
            index = i
    return index
def find_peak(mat):
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = m-1
    while low<=high:
        mid = (low+high)//2
        max_row = find_max_index(mat,n,m,mid)
        left = mat[max_row][mid-1] if mid-1>=0 else -1
        right = mat[max_row][mid+1] if mid+1<m else -1
        if mat[max_row][mid]>left and right<mat[max_row][mid]:
            return [max_row,mid]
        elif mat[max_row][mid]<left:
            high = mid-1
        else:
            low = mid+1
    return [-1,-1]
print(find_peak(mat))
