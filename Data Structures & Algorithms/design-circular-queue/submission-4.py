class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None, prev: Optional['ListNode'] = None):
        self.val = val
        self.next = next
        self.prev = prev



class MyCircularQueue:

    def __init__(self, k: int):
        self.length = 0
        self.maxlen = k
        self.head = None
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
            
        newtail = ListNode(value, None, self.tail)
        
        if self.isEmpty():
            self.head = newtail
            self.tail = newtail
        else:
            self.tail.next = newtail
            self.tail = newtail
            
        self.length += 1
        return True                

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.length -= 1
 
        self.head = self.head.next
        if not self.isEmpty():
            self.head.prev = None
        else:
            self.tail = None
        return True

        


    def Front(self) -> int:
        if self.head:
            return self.head.val     
        else:
            return -1

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val     
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.maxlen
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()