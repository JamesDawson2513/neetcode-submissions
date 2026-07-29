class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        self.dct = {}
        self.capacity = capacity
        
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_head(self, node: ListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        
        node = self.dct[key]
        self._remove(node)
        self._add_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            node = self.dct[key]
            node.val = value
            self._remove(node)
            self._add_head(node)
        else:
            if len(self.dct) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.dct[lru.key]
            
            new_node = ListNode(key, value)
            self.dct[key] = new_node
            self._add_head(new_node)