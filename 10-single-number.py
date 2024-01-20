# def single_number(nums):
#     temp = set()
#     for i in nums:
#         if i in temp:
#             temp.remove(i)
#         else:
#             temp.add(i)
#     print(temp.pop())

def single_number(nums):
    sum = 0
    for num in nums:
        sum = sum ^ num
    print(sum)

# Examples:

single_number([2, 2, 1])  # 1
single_number([4, 1, 2, 1, 2])  # 4
single_number([1])  # 1
