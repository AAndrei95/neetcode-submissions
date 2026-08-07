from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_num = -1

        for elem, cnt in counter.items():
            if cnt == 1 and elem > max_num:
                max_num = elem

        return max_num
                

        
