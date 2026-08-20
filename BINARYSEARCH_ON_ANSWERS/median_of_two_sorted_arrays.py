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