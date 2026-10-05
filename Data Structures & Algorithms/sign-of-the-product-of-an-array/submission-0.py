class Solution:
    def arraySign(self, nums: List[int]) -> int:
        self.nums = nums
        product = self.nums[0]

        for i in range(1, len(self.nums)):
            product *= self.nums[i]

        if product == 0:
            return 0
        
        return -1 if product < 0 else 1


        