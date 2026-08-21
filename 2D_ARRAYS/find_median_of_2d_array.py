def upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def count_small_equal(mat, x):
    count = 0

    for row in mat:
        count += upper_bound(row, x)

    return count


def median(mat):
    n = len(mat)
    m = len(mat[0])

    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)

    required = (n * m) // 2

    while low <= high:
        mid = (low + high) // 2

        count = count_small_equal(mat, mid)

        if count <= required:
            low = mid + 1
        else:
            high = mid - 1

    return low
arr = [[1,5,7,9,11],
       [2,3,4,5,10],
       [9,10,12,14,16]]
print(median(arr))