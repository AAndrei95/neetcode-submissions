from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        char_count = [x for x in Counter(s).values()]
        max_diff = -float("inf")

        for i in range(len(char_count)):
            for j in range(len(char_count)):
                if char_count[i] % 2 > 0 and char_count[j] % 2 == 0:
                    max_diff = max(max_diff, (char_count[i] - char_count[j]))
            
        return max_diff
         