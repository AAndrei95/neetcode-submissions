class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = decreasing = 0
        i_cnt = d_cnt = 1

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                i_cnt += 1
                increasing = max(increasing, i_cnt)
                d_cnt = 1

            if nums[i+1] < nums[i]:
                d_cnt += 1
                decreasing = max(decreasing, d_cnt)
                i_cnt = 1

            if nums[i+1] == nums[i]:
                i_cnt = d_cnt = 1
        
        if increasing == decreasing == 0:
            return i_cnt

        return increasing if increasing > decreasing else decreasing 
    
            


        