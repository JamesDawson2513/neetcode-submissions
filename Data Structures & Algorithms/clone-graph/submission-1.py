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
                if neighbor in nodeMap:
                    nodeMap[node].neighbors.append(nodeMap[neighbor])
                else:
                    newNeighbor = Node(neighbor.val, [])
                    nodeMap[neighbor] = newNeighbor
                    nodeMap[node].neighbors.append(newNeighbor)
                    q.append(neighbor)
        return nodeMap[head]