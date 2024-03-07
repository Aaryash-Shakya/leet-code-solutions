def is_valid_palindrome(s):
    s = s.lower()

    # Remove non-alphanumeric characters from the string
    new_str = ""
    for x in s:
        if x.isalnum():
            new_str += x

    # Check if the original string is equal to the reversed string
    rev_str = new_str[::-1]
    return new_str == rev_str


# Examples
# s = "A man, a plan, a canal: Panama"  # True
# s = "race a car"  # False
# s = " "  # True
