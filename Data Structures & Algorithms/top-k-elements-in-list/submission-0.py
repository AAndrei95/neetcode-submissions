from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums).most_common(k)
        values = []

        for i in range(len(nums_counter)):
            values.append(nums_counter[i][0])
        
        return values

        