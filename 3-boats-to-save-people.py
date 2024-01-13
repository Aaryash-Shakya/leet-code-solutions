def boats_to_save_people(people, limit):
    # sort people in ascending order of weight
    people.sort()

    # initialize left and right pointers and boats counter
    left = 0
    right = len(people) - 1
    boats = 0

    # while at least 2 people are left
    while left < right:
        # if both people can fit in the boat
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            boats += 1
        # if only the heavier person can fit in the boat
        else:
            right -= 1
            boats += 1
        """
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
        """

    # if there is 1 person left
    if left == right:
        boats += 1

    print(boats)


# Examples
people_1, limit_1 = [1, 2], 3
people_2, limit_2 = [3, 2, 2, 1], 3
people_3, limit_3 = [3, 5, 3, 4], 5

boats_to_save_people(people_1, limit_1)  # 1
boats_to_save_people(people_2, limit_2)  # 3
boats_to_save_people(people_3, limit_3)  # 4
