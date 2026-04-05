class MyHashMap:

    def __init__(self):
        self.key = []
        self.val = []

    def put(self, key: int, value: int) -> None:
        if key not in self.key:
            self.key.append(key)
            self.val.append(value)
            return

        idx = self.key.index(key)
        self.val[idx] = value
        
    def get(self, key: int) -> int:
        if key not in self.key:
            return -1
        idx = self.key.index(key)
        return self.val[idx]

    def remove(self, key: int) -> None:
        if key in self.key:
            idx = self.key.index(key)
            self.key.remove(key)
            self.val.remove(self.val[idx])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)