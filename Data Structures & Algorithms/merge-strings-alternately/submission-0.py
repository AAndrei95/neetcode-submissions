class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0, 0
        res = ""

        while n > 0 or m > 0:
            if n > 0:
                res += word1[i]
                i += 1
                n -= 1
            if m > 0:
                res += word2[j]
                j += 1
                m -= 1
        
        return res


        