def group_anagrams(strs):
    # initialize dictionary
    anagrams = {}
    for str in strs:
        # sort the string
        sorted_str = "".join(sorted(str))

        # if the sorted sequence already occurred, append the string to the list
        if sorted_str in anagrams:
            anagrams[sorted_str].append(str)
        # otherwise, create a new key-value pair
        else:
            anagrams[sorted_str] = [str]
            
    # return the values of the dictionary as a list
    return list(anagrams.values())


# Examples:
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams([""]))  # [[""]]
print(group_anagrams(["a"]))  # [["a"]]
