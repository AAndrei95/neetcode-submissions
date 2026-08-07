class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        cnt = 0

        for i in range(n, -1, -1):
            if s[i] != ' ':
                for j in range(i, -1, -1):
                    if s[j] != ' ':
                        cnt += 1
                    else:
                        return cnt
                return cnt