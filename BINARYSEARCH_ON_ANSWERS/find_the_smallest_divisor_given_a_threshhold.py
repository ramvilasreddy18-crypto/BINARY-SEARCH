# brute force solution
import math
arr = [1,2,5,9]
threshhold = 6
def divisor(arr,threshhold):
    for divisor in range(1,max(arr)):
        tot = 0
        for i in range(len(arr)):
            tot += math.ceil(arr[i]/divisor)
        if tot<=threshhold:
            return divisor
    return -1
print(divisor(arr,threshhold))
# optimal solution
import math
arr = [1,2,5,9]
threshhold = 6
def sum_of_divisors(arr,d):
    tot = 0
    for i in range(len(arr)):
        tot += math.ceil(arr[i]/d)
    return tot
def binary_search(arr,threshhold):
    low = 1
    high = max(arr)
    while low<=high:
        mid = (low+high)//2
        if sum_of_divisors(arr,mid)<=threshhold:
            high = mid-1
        else:
            low = mid+1
    return low
print(binary_search(arr,threshhold))