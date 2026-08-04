class PrefixTree:

    def __init__(self):
        self.starting = {}

    def insert(self, word: str) -> None:
        cur = self.starting
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['_'] = True

    def search(self, word: str) -> bool:
        cur = self.starting
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return '_' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.starting
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True
        