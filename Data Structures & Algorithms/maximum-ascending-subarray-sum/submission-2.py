class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_subarray = 0
        idx = 0

        if len(nums) == 1 or nums.count(nums[0]) == len(nums):
            return nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                max_subarray = max(max_subarray, sum(nums[idx:i+1]))
            else:
                idx = i
        
        return max_subarray if max_subarray > 0 else max(nums)
            

        