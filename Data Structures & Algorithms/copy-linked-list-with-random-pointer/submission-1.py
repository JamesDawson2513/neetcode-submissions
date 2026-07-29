"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        nodehash = {}
        while dummy:
            nodehash[dummy] = Node(dummy.val)
            dummy = dummy.next
        nodehash[None] = None
        dummy = head
        while dummy:
            nodehash[dummy].next = nodehash[dummy.next]
            nodehash[dummy].random = nodehash[dummy.random]
            dummy = dummy.next
        return nodehash[head]
