"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, head: Optional['Node']) -> Optional['Node']:
        if not head:
            return None
        nodeMap = {}
        nodeMap[head] = Node(head.val, [])
        q = collections.deque()
        q.append(head)
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in nodeMap:
                    newNeighbor = Node(neighbor.val, [])
                    nodeMap[neighbor] = newNeighbor
                    q.append(neighbor)
                nodeMap[node].neighbors.append(nodeMap[neighbor])
        return nodeMap[head]