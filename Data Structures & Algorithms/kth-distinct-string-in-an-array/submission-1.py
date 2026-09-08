from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        word_count = Counter(arr)
        distinct = []

        for char, freq in word_count.items():
            if freq == 1:
                distinct.append(char)

        if len(distinct) > 0 and k <= len(distinct):
            return distinct[k-1]
        
        return ""
        
        