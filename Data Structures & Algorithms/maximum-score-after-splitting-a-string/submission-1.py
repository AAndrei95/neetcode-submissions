from collections import Counter

class Solution:
    def maxScore(self, s: str) -> int:
        l_zeros, r_ones = 0, s.count("1")
        max_score = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                l_zeros += 1
            else:
                r_ones -= 1
                
            max_score = max(max_score, (l_zeros + r_ones))

        return max_score

        


            
        