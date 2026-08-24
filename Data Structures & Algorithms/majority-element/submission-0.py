from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_elem = Counter(nums).most_common(1)

        return max_elem[0][0]


        