class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers():
    result = ListNode(0)
    tail = result
    carry =0
    while l1 != None or l2 != None or carry == 1:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        sum = (digit1 + digit2 + carry)
        lastDigit = sum%10
        carry = sum // 10

        tail.next = ListNode(lastDigit)
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    return result.next