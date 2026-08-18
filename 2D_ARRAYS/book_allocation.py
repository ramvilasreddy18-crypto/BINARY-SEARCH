arr = [12,34,67,90]
k = 2
def allocation_is_possible(arr,barrier,k):
    allocated_stu = 1
    pages = 0
    for i in range(len(arr)):
        if (arr[i]>barrier):
            return False
        if (pages+arr[i])>barrier:
            allocated_stu += 1
            pages = arr[i]
        else:
            pages += arr[i]
    if allocated_stu>k :
        return False
    else:
        return True
def book_allocation(arr,k):
    low = max(arr)
    high = sum(arr)
    while low<=high:
        mid = (low+high)//2
        if (allocation_is_possible(arr,mid,k)):
            high = mid-1
        else:
            low = mid+1
    return low
print(book_allocation(arr,k))
