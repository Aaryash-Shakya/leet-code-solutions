def contains_duplicate(nums):
    # initialize and empty set
    num_set = set()

    for num in nums:
        # if num has already occurred
        if num in num_set:
            return True
        num_set.add(num)

    # program control exits the loop if no duplicate is found
    return False


# Examples:
print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
