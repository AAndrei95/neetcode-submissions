class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)

        if haystack == needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i:k+i] == needle:
                return i
        
        return -1
        