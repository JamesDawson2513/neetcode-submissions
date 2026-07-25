class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.freq.get(val, 0) + 1

    def pop(self) -> int:
        maxfreq = max(self.freq.values())
        
        # 1. Scan backwards to find the index of the most recent maxfreq element
        n = len(self.stack)
        target_idx = -1
        for i in range(n - 1, -1, -1):
            if self.freq[self.stack[i]] == maxfreq:
                target_idx = i
                break
                
        maxval = self.stack[target_idx]
        
        # 2. Pop exactly the elements above target_idx into temp
        temp = []
        num_to_pop = (n - 1) - target_idx
        for _ in range(num_to_pop):
            temp.append(self.stack.pop())
            
        # 3. Pop the target element itself
        self.stack.pop()
        self.freq[maxval] -= 1
        
        # 4. Restore elements from temp
        while temp:
            self.stack.append(temp.pop())
            
        return maxval