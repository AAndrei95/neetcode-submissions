class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        n = len(s)-1
        g.sort(reverse=True)
        s.sort()

        if n == 0:
            return 1 if 1 in g else 0

        for child in g:
            if n >= 0:
                if child <= s[n]:
                    res += 1
                    n -= 1
            
        return res
        