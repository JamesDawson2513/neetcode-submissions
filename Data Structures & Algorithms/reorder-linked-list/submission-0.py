# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        for i in range(((length-1) // 2) + 1):
            curr = curr.next
        rev = None
        while curr:
            temp = rev
            rev = ListNode(curr.val)
            rev.next = temp
            curr = curr.next
        dummy = res =  ListNode()
        dummy.next = head
        for i in range(length):
            if i % 2 == 0:
                res.next = head
                head = head.next
                res = res.next
                res.next = None
            else:
                res.next = rev
                rev = rev.next
                res = res.next
                res.next = None
        head = dummy.next

                

        
