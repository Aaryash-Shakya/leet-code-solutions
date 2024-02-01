def reverse_list(head):
    # Initialize two pointers: prev (previous) and curr (current).
    prev = None
    curr = head

    # Iterate through the list to reverse the links.
    while curr is not None:
        # Temporarily store the next node.
        temp = curr.next

        # Update the next pointer of the current node to point to the previous node.
        curr.next = prev

        # Move prev and curr pointers one step forward.
        prev = curr
        curr = temp

    # Return prev, which now points to the new head of the reversed list.
    return prev

# Examples:
# reverse_list([1, 2, 3, 4, 5])  # [5, 4, 3, 2, 1]
# reverse_list([1, 2])  # [2, 1]
