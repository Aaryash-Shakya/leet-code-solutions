"""
def merge_array(nums1, m, nums2, n):
    # copy nums2 to zero spaces of nums1
    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()
    print(nums1)
"""


# merge from the end of the array
def merge_array(nums1, m, nums2, n):
    i, j = m - 1, n - 1
    last = m + n - 1
    # while either nums1 or num2 is not empty
    # compare the last elements of nums1 and nums2
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
            last -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
    # if nums2 is not empty, copy the rest of nums2 to nums1
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1
    

# Examples:
merge_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)  # [1, 2, 2, 3, 5, 6]
merge_array([1], 1, [], 0)  # [1]
merge_array([0], 0, [1], 1)  # [1]
