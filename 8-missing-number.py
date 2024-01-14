def missing_number(nums):
    # initialize a set
    numSet = set()
    # add numbers from 0 to len(nums) in the set
    for i in range(0, len(nums)):
        numSet.add(i)

    # remove numbers from the set that are in nums
    for i in nums:
        if i in numSet:
            numSet.remove(i)

    # if no number is remaining, return the next number in the sequence
    if len(numSet) == 0:
        print(len(nums))
    # else return the remaining number
    else:
        print(numSet.pop())


# Examples:
missing_number([3, 0, 1])  # 2
missing_number([0, 1])  # 2
missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])  # 8
