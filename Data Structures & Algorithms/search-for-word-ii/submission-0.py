class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = w

class Solution:
    def adj(self,i,j,m,n) -> List[List[int]]:
        adjacent = []
        if i > 0:
            adjacent.append([i-1, j])
        if i < m-1:
            adjacent.append([i+1, j])
        if j > 0:
            adjacent.append([i, j-1])
        if j < n-1:
            adjacent.append([i, j + 1])
        return adjacent
            

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = Trie(words).root
        res = []
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, curr: TrieNode):
            char = board[i][j]
            if char not in curr.children:
                return

            next_node = curr.children[char]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[i][j] = "#"

            for ni, nj in self.adj(i, j, m, n):
                if board[ni][nj] != "#":
                    dfs(ni, nj, next_node)

            board[i][j] = char

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res