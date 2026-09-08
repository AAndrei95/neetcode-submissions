from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        word_count = Counter(arr)
        distinct = []

        for char, freq in word_count.items():
            if freq == 1:
                distinct.append(char)

        for string in arr:
            if string in distinct:
                k -= 1
            
            if k == 0:
                return string
        
        return ""
        
        