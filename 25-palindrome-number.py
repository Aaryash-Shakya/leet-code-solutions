def palindrome_number(x):
    str_x = str(x)
    rev_str_x = str_x[::-1]
    return str_x == rev_str_x


# Examples:
# palindrome_number(121)  # True
# palindrome_number(-121)  # False
# palindrome_number(10)  # False
