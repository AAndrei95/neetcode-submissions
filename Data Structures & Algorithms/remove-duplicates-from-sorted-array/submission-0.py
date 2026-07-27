class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)-1
        slow = 0
        fast = 1

        for i in range(n):
            if nums[slow] == nums[fast]:
                fast += 1
            elif nums[slow] != nums[fast]:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
        return slow + 1
           





        