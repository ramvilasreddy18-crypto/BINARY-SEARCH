# brute force solution 
piles = [3,6,7,11]
h = 8
def hours(piles, speed):
    total = 0

    for pile in piles:
        total += (pile + speed - 1) // speed

    return total

def koko(piles, h):
    for speed in range(1, max(piles) + 1):
        req_time = hours(piles, speed)

        if req_time <= h:
            return speed

print(koko(piles, h))
# optimal solution using binary search
import math
piles = [3,6,7,11]
h = 8
def calculate_total_hours(piles,hours):
    totalhours = 0
    for i in range(len(piles)):
        totalhours += math.ceil(piles[i]/hours)
    return totalhours
def koko(piles,h):
    low = 1
    high = max(piles)
    while low<=high:
        mid = (low+high)//2
        totalhours = calculate_total_hours(piles,mid)
        if totalhours<=h:
            high = mid-1
        else:
            low = mid+1
    return low
print(koko(piles,h))
