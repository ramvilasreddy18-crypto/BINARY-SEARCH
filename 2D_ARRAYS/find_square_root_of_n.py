# brute force solution
n = 35
ans = 1
for i in range(n):
    if (i*i <= n):
        ans = i
    else:
        break
print(ans)
# optimal solution using binary search
n = 35
def square_root(n):
    low = 1
    high = n
    while (low<=high):
        mid = (low+high)//2
        if ((mid*mid)<=n):
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return high
print(square_root(n))
