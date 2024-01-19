def single_number(arr):
    temp = set()
    for i in arr:
        if i in temp:
            temp.remove(i)
        else:
            temp.add(i)
    print(temp.pop())


single_number([2, 2, 1])  # 1
single_number([4, 1, 2, 1, 2])  # 4
single_number([1])  # 1
