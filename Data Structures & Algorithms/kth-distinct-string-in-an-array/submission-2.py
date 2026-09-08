from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        word_count = Counter(arr)

        for char, freq in word_count.items():
            if freq == 1:
                k -= 1
            
            if k == 0:
                return char
        
        return ""
        
        