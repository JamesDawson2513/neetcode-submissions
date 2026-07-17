# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        dNode = {}
        carry = 0
        while l1 or l2 or carry:
            if l1 == None and l2 == None:
                dNode[i] = ListNode(1)
                dNode[i-1].next = dNode[i]
                dNode[i].next = None
                return dNode[0]
            elif l1 == None:
                tot = l2.val + carry
            elif l2 == None:
                tot = l1.val + carry
            else:
                tot = l1.val + l2.val + carry
            dNode[i] = ListNode((tot) % 10) 
            carry = (tot//10)
            i += 1
            if i != 1:
                dNode[i-2].next = dNode[i-1]
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next      
        return dNode[0]
            

        