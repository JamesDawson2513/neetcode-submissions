class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustLog = {} #Stores arrays [num trustees, num trusters]
        for i in range(len(trust)):
            trustLog[trust[i][0]] = [trustLog.get(trust[i][0], [0,0])[0] + 1, trustLog.get(trust[i][0], [0,0])[1]]
            trustLog[trust[i][1]] = [trustLog.get(trust[i][1], [0,0])[0], trustLog.get(trust[i][1], [0,0])[1] + 1]
            print(trustLog)
        for i in range(n):
            if trustLog.get(i + 1, [0,0]) == [0, n-1]:
                return i + 1
        return -1 
        
            