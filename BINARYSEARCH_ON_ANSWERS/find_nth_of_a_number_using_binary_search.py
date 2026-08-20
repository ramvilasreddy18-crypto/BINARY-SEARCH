def multiply(num,n):
    ans = 1
    for _ in range(n):
        ans *= num
    return ans
def get_nth_root(n,m):
    low = 1
    high = m
    eps = 1e-6
    while high-low>eps:
        mid = (low+high)/2
        if multiply(mid,n)<m:
            low = mid
        else:
            high = mid
    return low
n = 3
m = 27
print(get_nth_root(n,m))
