def binary_search(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = int((l + r) / 2)
        if arr[m] == key:
            # key found
            return m
        elif key < arr[m]:
            r = m - 1
        else:
            l = m + 1
    # key not found
    return False


def first_last_position(arr, key):
    first = -1
    last = -1

    # binary search
    i = binary_search(arr, key)

    # key found
    if i != False:
        first = i
        last = i

        # iterate to find the first occurrence
        while arr[first - 1] == key:
            first = first - 1

        # iterate to find the last occurrence
        while arr[last + 1] == key:
            last = last + 1

    print([first, last])


# Examples:
arr_1, key_1 = [5, 7, 7, 8, 8, 10], 8
arr_2, key_2 = [5, 7, 7, 8, 8, 10], 6
arr_3, key_3 = [], 0

first_last_position(arr_1, key_1)  # [3, 4]
first_last_position(arr_2, key_2)  # [-1, -1]
first_last_position(arr_3, key_3)  # [-1, -1]
