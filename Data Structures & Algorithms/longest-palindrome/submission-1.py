from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        sCounter = Counter(s)
        res = 0
        max_flag = 0

        for char, freq in sCounter.items():
            res += (freq // 2) * 2
            
            if freq % 2 != 0:
                max_flag = 1
        
        return res + max_flag
                


        

        