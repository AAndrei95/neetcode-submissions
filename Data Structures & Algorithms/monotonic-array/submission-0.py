class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc, dec = 1, 1

        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                dec += 1
            
            if nums[i-1] <= nums[i]:
                inc += 1

        return inc == n if inc > dec else dec == n


