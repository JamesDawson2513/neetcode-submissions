class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        left_prev = dummy

        curr = head
        
        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next

        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next