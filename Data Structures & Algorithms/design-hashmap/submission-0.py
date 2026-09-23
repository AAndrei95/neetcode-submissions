class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
        
    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            self.values[idx] = value
        else:
            self.keys.append(key)
            self.values.append(value)  
   
    def get(self, key: int) -> int:
        if key in self.keys:
            idx = self.keys.index(key)
            return self.values[idx]
        
        return -1
        
    def remove(self, key: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            self.values.pop(idx)
            self.keys.pop(idx)
   
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)