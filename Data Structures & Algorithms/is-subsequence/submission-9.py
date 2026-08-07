class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        result = ""
        idx = 0

        for i in range(len(t)):
            if t[i] == s[idx]:
                result += s[idx]
                idx += 1
                if result == s:
                    return True

        return s == result

        