def len_last_word(s):
    # Split the string into a list of words
    words = s.split()
    last_word = words[-1]
    
    # Return the length of the last_word
    return len(last_word)


# Examples:
# s = "Hello World"  # 5
# s = "   fly me   to   the moon  " # 4
# s = "luffy is still joyboy" # 6
