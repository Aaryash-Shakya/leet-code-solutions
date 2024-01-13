def longest_substring(S):
    # initialization
    max_length = 0
    wl = 0

    # window set to store characters in window
    window = set()

    # iterate through the string
    for wr in range(len(S)):
        # while current element is a duplicate, remove elements from the left of window
        while S[wr] in window:
            window.remove(S[wl])
            wl += 1

        # add the current element to the window
        window.add(S[wr])

        # window length = wr - wl + 1 OR len(window)
        # update max_length if current window length is greater
        max_length = max(max_length, len(window))

# Examples
S_1 = "abcabcbb"
S_2 = "bbbbb"
S_3 = "pwwkew"

print(longest_substring(S_1))  # 3
print(longest_substring(S_2))  # 1
print(longest_substring(S_3))  # 3