# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(list1, list2):
        merged = ListNode()
        last = merged

        # while both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next
            else:
                last.next = list2
                list2 = list2.next
            last = last.next

        # append the remaining nodes from list1 or list2
        if list1:
            last.next = list1
        elif list2:
            last.next = list2

        return merged.next
    
# Examples:
# list1 = [1, 2, 4], list2 = [1, 3, 4]  # [1, 1, 2, 3, 4, 4]
# list1 = [], list2 = []  # []
# list1 = [], list2 = [0]  # [0]