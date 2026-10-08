from collections import Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.numsCounter = Counter(nums)
        
    def showFirstUnique(self) -> int:
        for num in self.nums:
            if self.numsCounter[num] == 1:
                return num
        return -1
        
    def add(self, value: int) -> None:
        self.nums.append(value)
        self.numsCounter = Counter(self.nums)
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
