def majority_element(nums):
    nums.sort()
    mid = int(len(nums) / 2)
    return nums[mid]


# Examples:
print(majority_element([3, 2, 3]))  # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
print(majority_element([1]))  # 1
