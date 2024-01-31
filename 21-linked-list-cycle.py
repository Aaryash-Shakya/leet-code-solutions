# Floyd's Tortoise and Hare Algorithm
def linked_list_cycle(head):
    # initialize two pointers
    slow = head
    fast = head

    # until fast pointer reaches the end of the list
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        # if two pointers meet
        if slow == fast:
            return True

    # executed if fast pointer reaches the end of the list
    return False


# Examples: (array is just a placeholder for ListNode)
linked_list_cycle([3, 2, 0, -4])  # True
linked_list_cycle([1, 2])  # True
linked_list_cycle([1])  # False
