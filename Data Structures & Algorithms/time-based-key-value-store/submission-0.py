class TimeMap:

    def __init__(self):
        self.dict = {}
        self.keymax = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = {}
            self.keymax[key] = timestamp
        self.dict[key][timestamp] = value
        self.keymax[key] = max(self.keymax[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ''
        if timestamp >= self.keymax[key]:
            return self.dict[key][self.keymax[key]]
        while timestamp >= 0:
            if timestamp in self.dict[key]:
                return self.dict[key][timestamp]
            else:
                timestamp -= 1
        return ''
