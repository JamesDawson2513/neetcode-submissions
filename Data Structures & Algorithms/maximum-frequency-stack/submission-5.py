class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] =  self.freq.get(val, 0) + 1

    def pop(self) -> int:
        maxfreq = max(self.freq.values())
        maxval = -1
        i = 0
        while maxval == -1:
            n = len(self.stack)
            if self.freq[self.stack[n-1-i]] == maxfreq:
                maxval = self.stack[n-1-i]
            i += 1
        temp = []
        for _ in range(i-1):
            temp.append(self.stack.pop())
        self.stack.pop()
        self.freq[maxval] -= 1
        while temp:
            self.stack.append(temp.pop())
        return maxval
        



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()