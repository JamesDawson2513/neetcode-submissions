class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0 or len(matchsticks) < 4:
            return False

        target = total_len // 4

        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return True

            for j in range(4):

                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]  
                    
                if sides[j] == 0:
                    break

            return False

        return dfs(0)