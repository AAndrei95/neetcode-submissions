from collections import Counter

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if Counter(s).most_common()[0][1] == 1:
            return -1

        max_dist = 0
        for i in range(len(s)):
            if max_dist > len(s) - i:
                break
            for j in range(len(s)-1, -1, -1):
                if s[i] == s[j]:
                    max_dist = max(max_dist, (j-1) - i)
                    break
        
        return max_dist

        