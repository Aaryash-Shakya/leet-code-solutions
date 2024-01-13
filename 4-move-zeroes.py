# approach 1
'''
def move_zeroes(integer):
    temp = []

    # append non-zero elements to temp
    for num in integer:
        if num != 0:
            temp.append(num)

    # append remaining zeroes to temp
    for i in range(len(temp), len(integer)):
        temp.append(0)

    # change the original list
    integer[:] = temp
    print(integer)
'''
def move_zeroes(integer):

    # initialize pointer to track position for next non-zero element
    non_zero_index = 0
    
    # Iterate through the array
    for num in integer:
        # Move non-zero element to the current non_zero_index and increment it
        if num != 0:
            integer[non_zero_index] = num
            non_zero_index += 1
    
    # Fill the remaining positions with zeros
    for i in range(non_zero_index, len(integer)):
        integer[i] = 0

    print(integer)

# Examples
integer_1 = [0, 1, 0, 3, 12]
integer_2 = [0, 0, 0, 0, 0]
integer_3 = [1, 2, 3, 4, 5]

move_zeroes(integer_1)  # [1, 3, 12, 0, 0]
move_zeroes(integer_2)  # [0, 0, 0, 0, 0]
move_zeroes(integer_3)  # [1, 2, 3, 4, 5]

# integer[:] = temp changes the original list
print(integer_1)  # [1, 3, 12, 0, 0]
