# class Node:
#     def __init__(self,key, val):
#         self.key, self.val = key,val
#         self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if self.cap < len(self.cache): # we are deleting the element at loc 0
            self.cache.popitem(last=False)


