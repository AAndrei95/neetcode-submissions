class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                rotated_nums = nums[i:] + nums[:i]
                return  rotated_nums == sorted(nums)

        return True