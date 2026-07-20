class MyQueue:

    def __init__(self):
        self.stack = []       

    def push(self, x: int) -> None:
        self.stack.append(x)        

    def pop(self) -> int:
        stack2 = []
        for i in range(len(self.stack) - 1):
            stack2.append(self.stack.pop())

        res = self.stack.pop()

        for i in range(len(stack2)):
            self.stack.append(stack2.pop())
        return res

    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()