# counting approach O(2n)
'''
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
'''

# dutch national flag algorithm O(n)
# slightly better as it only traverses the list once
def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <=high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] ==1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Examples:
# sort_colors([2, 0, 2, 1, 1, 0]) = [0, 0, 1, 1, 2, 2]
# sort_colors([2, 0, 1]) = [0, 1, 2]
