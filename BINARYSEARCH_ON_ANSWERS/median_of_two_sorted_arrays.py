# brute force solution 
arr1 = [1,3,4,7,10,12]
arr2 =[2,3,6,15]
def find_median(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    total = n1+n2
    i = j = 0
    cur = prev = 0
    for k in range(total//(2)+1):
        prev = cur
        if i<n1 and (j>=n2 or arr1[i]<=arr2[j]):
            cur = arr1[i]
            i+=1
        else:
            cur = arr2[j]
            j+=1
    if total%2 == 0:
        return (cur+prev)/2
    else:
        return cur
# binary search 
arr1 = [1,3,4,7,10,12]
arr2 =[2,3,6,15]
def find_median_sorted(arr1,arr2):
    if len(arr1)>len(arr2):
        return find_median_sorted(arr2,arr1)
    n1 = len(arr1)
    n2 = len(arr2)
    low = 0
    high = n1
    while low<=high:
        cut1 = (low+high)//2
        cut2 = (n1+n2+1)//2-cut1
        left1 = float('-inf') if cut1 == 0 else arr1[cut1-1]
        right1 = float('inf') if cut1 == n1 else arr1[cut1]

        left2 = float('-inf') if cut2 == 0 else arr2[cut2-1]
        right2 = float('inf') if cut2 == n2 else arr2[cut2]

        if left1 <= right2 and left2 <= right1:
            if (n1+n2)%2 == 0:
                 return (max(left1,left2)+min(right1,right2))/2
            else:
                return max(left1,left2)
        elif left1>right2:
            high = cut1 - 1
        else:
            low = cut1+1
print(find_median_sorted(arr1,arr2))    