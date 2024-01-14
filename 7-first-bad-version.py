def isBadVersion(version):
    return version >= 4


# binary search
def first_bad_version(n):
    left = 1
    right = n
    while left <= right:
        mid = int((left + right) / 2)

        # if mid is the first bad version
        if isBadVersion(mid) and (not isBadVersion(mid - 1) or mid == 1):
            print(mid)
            break

        # if mid is a bad version but not the first bad version
        elif isBadVersion(mid):
            right = mid - 1
        
        # if mid is not a bad version
        else:
            left = mid + 1


# linear
# def first_bad_version(n):
#     for i in range(1, n):
#         if isBadVersion(i):
#             print(i)
#             break


# Examples:
first_bad_version(5)  # 4
first_bad_version(10)  # 4
