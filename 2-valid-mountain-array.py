def valid_mountain(array):
    # check length of array
    length = len(array)
    if length < 3:
        return False

    # initialize left and right pointers
    left = 0
    right = length - 1

    # while
    # left + 1 is less than last index and
    # left + 1 element is larger than left element
    while (left + 1 < length - 1) and (array[left] < array[left + 1]):
        # increment left pointer
        left += 1

    # while
    # right - 1 is greater than first index and
    # right - 1 element is larger than right element
    while (right - 1 > 0) and (array[right - 1] > array[right]):
        # decrement right pointer
        right -= 1

    # check if left and right converges to same peak
    if left == right:
        return True
    else:
        return False


# Examples
mountain_1 = [1, 2, 3, 2, 1]
mountain_2 = [1, 2, 3, 4, 5]
mountain_3 = [5, 4, 3, 2, 1]
mountain_4 = [1, 2, 3, 4, 3, 2, 1]

print(valid_mountain(mountain_1))  # True
print(valid_mountain(mountain_2))  # False
print(valid_mountain(mountain_3))  # False
print(valid_mountain(mountain_4))  # True
