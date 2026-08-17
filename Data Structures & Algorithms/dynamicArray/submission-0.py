class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        if i < self.capacity:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        
    def popback(self) -> int:
        if len(self.arr) > 0:
            temp = self.arr[self.size-1]
            self.arr[self.size-1] = 0
            self.size -= 1
            return temp

    def resize(self) -> None:
        self.arr = self.arr + [0] * len(self.arr)
        self.capacity = len(self.arr)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)
