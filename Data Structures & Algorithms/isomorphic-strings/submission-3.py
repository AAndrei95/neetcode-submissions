class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars = {}

        for i in range(len(t)):
            if s[i] not in chars.keys():
                if t[i] in chars.values():
                    return False
                else:
                    chars[s[i]] = t[i]

            elif s[i] in chars.keys():
                if chars[s[i]] == t[i]:
                    pass
                else:
                    return False
        
        return True



