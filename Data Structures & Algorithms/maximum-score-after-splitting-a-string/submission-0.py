from collections import Counter

class Solution:
    def maxScore(self, s: str) -> int:
        posibilities = {}
        max_score = 0

        for i in range(1, len(s)):
            posibilities[s[:i]] = s[i:]
        
        for key, value in posibilities.items():
            left = Counter(key)
            right = Counter(value)
            max_score = max(max_score, (left["0"]+right["1"]))

        return max_score

        


            
        