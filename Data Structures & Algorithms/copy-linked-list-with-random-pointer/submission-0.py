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
        cur = head
        dnode = {}
        dnode[None] = None
        while cur:
            copy = Node(cur.val)
            dnode[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            dnode[cur].next = dnode[cur.next]
            dnode[cur].random = dnode[cur.random]
            cur = cur.next
        return dnode[head]
        


        