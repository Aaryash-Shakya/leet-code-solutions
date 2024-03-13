# counting approach O(n)
def sort_colors(nums):
    # initialize counters
    count_0, count_1, count_2 = 0, 0, 0

    # count occurrences of 0, 1, and 2
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    # update nums list to make them sorted
    for i in range(len(nums)):
        if i < count_0:
            nums[i] = 0
        elif i < count_0 + count_1:
            nums[i] = 1
        else:
            nums[i] = 2


# Examples:
# sort_colors([2, 0, 2, 1, 1, 0]) = [0, 0, 1, 1, 2, 2]
# sort_colors([2, 0, 1]) = [0, 1, 2]
