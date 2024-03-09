def searchInsert(nums, target):
    # initialize the left and right pointers
    left = 0 
    right = len(nums) - 1

    # perform binary search until left and right pointers meet
    while left <= right:  
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1 
        else:
            left = mid + 1 

    # return the index where the target should be inserted if not found
    return left  


# Examples:
# searchInsert([1,3,5,6], 5)  # 2
# searchInsert([1,3,5,6], 2)  # 1
# searchInsert([1,3,5,6], 7)  # 4
