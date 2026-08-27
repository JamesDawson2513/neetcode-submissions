class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = collections.deque()
        visited = {"0000"}
        dead_set = set(deadends)
        if target == "0000":
            return 0
        elif "0000" in dead_set:
            return -1
        q.append("0000")
        turns = 0
        while q:
            turns += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(4):
                    digit = int(cur[i])
                    for d in [-1,1]:
                        change = (digit + d) % 10
                        new = cur[:i] + str(change) + cur[i+1:]
                        if new == target:
                            return turns
                        elif new in dead_set or new in visited:
                            continue
                        else:
                            q.append(new)
                            visited.add(new)
        return -1
