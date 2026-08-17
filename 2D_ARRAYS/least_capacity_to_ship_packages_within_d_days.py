# brute force solution
# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
# def min_capacity(weights,days):
#     for i in range(max(weights),sum(weights)+1):
#         daysneed = daysrequired(weights,i)
#         if daysneed<=days:
#             return i
# def daysrequired(weights,capacity):
#     dayreq = 1
#     load = 0
#     for i in range(len(weights)):
#         if load+weights[i]>capacity:
#             dayreq += 1
#             load = weights[i]
#         else:
#             load += weights[i]
#     return dayreq
# print(min_capacity(weights,days))
# optimal solution
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
def daysrequired(weights,capacity):
    dayreq = 1
    load = 0
    for i in range(len(weights)):
        if load+weights[i]>capacity:
            dayreq += 1
            load = weights[i]
        else:
            load += weights[i]
    return dayreq
def min_days(weights,days):
    low = max(weights)
    high = sum(weights)
    while low<=high:
        mid = (low+high)//2
        no_of_days = daysrequired(weights,mid)
        if no_of_days<=days:
            high = mid-1
        else:
            low = mid+1
    return low
print(min_days(weights,days))