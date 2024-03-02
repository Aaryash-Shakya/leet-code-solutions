def isValid(s):
    stack = []
    for char in s:
        # If the character is an opening bracket, we push it onto the stack
        if char in ["(", "{", "["]:
            stack.append(char)

        # If the character is a closing bracket, we pop the last element from the stack and check if it matches the corresponding opening bracket
        elif char == ")":
            if stack.pop() != "(":
                return False
        elif char == "}":
            if stack.pop() != "{":
                return False
        elif char == "]":
            if stack.pop() != "[":
                return False
    if not stack:
        return True


# Examples:
# s = "()"  # True
# s = "()[]{}"  # True
# s = "(]"  # False
