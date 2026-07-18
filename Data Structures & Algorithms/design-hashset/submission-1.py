class MyHashSet:

    def __init__(self):
        self.num_buckets = 10000
        self.buckets = [[] for _ in range(self.num_buckets)]

    def hash(self,key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket = self.hash(key)
        if key not in self.buckets[bucket]:
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = self.hash(key)
        self.buckets[bucket] = []
        
    def contains(self, key: int) -> bool:
        bucket = self.hash(key)
        if self.buckets[bucket] == []:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)