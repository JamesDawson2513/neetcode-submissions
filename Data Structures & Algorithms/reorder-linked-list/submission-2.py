# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur, count = head, 0
        while cur:
            cur = cur.next
            count += 1
        cur = head
        for i in range((count - 1)//2):
            cur = cur.next
        prev = cur
        cur = cur.next
        prev.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        first = head
        second = prev
        while first and second:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp
        
            

        
        