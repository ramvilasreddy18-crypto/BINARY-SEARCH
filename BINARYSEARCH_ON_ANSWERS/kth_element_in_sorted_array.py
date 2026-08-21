def kth_element(nums1, nums2, k):
    if len(nums1) > len(nums2):
        return kth_element(nums2, nums1, k)

    n1 = len(nums1)
    n2 = len(nums2)

    low = max(k - n2, 0)
    high = min(k, n1)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1

        left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        right1 = float('inf') if cut1 == n1 else nums1[cut1]

        left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        right2 = float('inf') if cut2 == n2 else nums2[cut2]

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1

        else:
            low = cut1 + 1


nums1 = [2, 3, 6, 7, 9]
nums2 = [1, 4, 8, 10]

print(kth_element(nums1, nums2, 5))