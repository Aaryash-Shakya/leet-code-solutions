def add_digits(num):
    sum = 0
    while num > 0:
        # get the last digit of num
        last_digit = num % 10
        sum += last_digit

        # remove the last digit from num
        num = num // 10

        # if num is 0 and the sum is greater than 9, set num to sum and reset sum to 0
        if num == 0 and sum > 9:
            num = sum
            sum = 0
    return sum


# Examples:
# add_digits(38)  # 2
# add_digits(0)  # 0
# add_digits(123)  # 6
