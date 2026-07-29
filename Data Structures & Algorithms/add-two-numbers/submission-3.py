# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        store = 0
        head = dummy
        while l1 and l2:
            sum = l1.val + l2.val + store
            head.next = ListNode(sum % 10)
            store = (sum // 10)
            l1, l2, head = l1.next, l2.next, head.next
        while l1:
            sum = l1.val + store
            head.next = ListNode(sum % 10)
            l1, head = l1.next, head.next
            store = sum // 10
        while l2:
            sum = l2.val + store
            head.next = ListNode(sum % 10)
            l2, head = l2.next, head.next
            store = sum // 10
        if store == 1:
            head.next = ListNode(1)
        return dummy.next