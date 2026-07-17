# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tf = tl = head
        for _ in range(n):
            tl = tl.next
        if tl == None:
            return tf.next
        while tl.next:
            tf = tf.next
            tl = tl.next
        tf.next = tf.next.next
        return head