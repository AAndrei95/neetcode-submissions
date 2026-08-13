from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_counter = Counter(nums)

        for num, freq in num_counter.items():
            if freq % 2 > 0:
                return False
                
        return True

        