class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.values = []

    def next(self, val: int) -> float:
        self.values.append(val)
        
        return sum(self.values[-self.size:]) / min(len(self.values), self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
