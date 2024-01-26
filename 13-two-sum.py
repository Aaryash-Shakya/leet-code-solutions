def two_sum(nums, target):
    for i in range(len(nums)):
        # assume i is part of solution

        # check sum of ith element with every element after i
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])


# Examples:
two_sum([2, 7, 11, 15], 9)  # [0,1]
two_sum([3, 2, 4], 6)  # [1,2]
two_sum([3, 3], 6)  # [0,1]
