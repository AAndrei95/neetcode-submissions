from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        str_counter = Counter(s)
        cnt = 0

        for char, freq in str_counter.items():
            if freq % 2:
                cnt += 1
        
        return cnt == 1 or cnt == 0
                    
            
        