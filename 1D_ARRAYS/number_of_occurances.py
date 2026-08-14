arr = [1,2,3,3,5,8,8,10,10,11]
x = 10
n = len(arr)
def first_occurance(arr,n,x):
    low = 0
    high = n-1
    first = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == x:
            first = mid
            high = mid-1
        elif arr[mid]>x:
            high = mid-1
        else:
            low = mid+1
    return first
def last_occurance(arr,n,x):
    low = 0
    high = n-1
    last = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == x:
            last = mid
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
        else:
            low = mid+1
    return last
def number_of_occurances(arr,x,n):
    first = first_occurance(arr,x,n)
    if first == -1:
        return 0
    last = last_occurance(arr,x,n)
    return (last-first)+1
print(number_of_occurances(arr,x,n))



