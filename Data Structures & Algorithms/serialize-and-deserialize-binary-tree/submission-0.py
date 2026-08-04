# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = []
        q = collections.deque()
        q.append(root)
        node = root
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append('B')
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))

        q = collections.deque([root])

        i = 1

        while q and i < len(nodes):
            parent = q.popleft()

            if nodes[i] != 'B':
                left_child = TreeNode(int(nodes[i]))
                parent.left = left_child
                q.append(left_child)
            
            i += 1

            if i < len(nodes) and nodes[i] != 'B':
                right_child = TreeNode(int(nodes[i]))
                parent.right = right_child
                q.append(right_child)

            i += 1

        return root
