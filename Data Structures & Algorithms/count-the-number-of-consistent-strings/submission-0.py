from collections import Counter

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = []

        for i in range(len(words)):
            is_ = True
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    is_ = False
                    break
            if is_:
                res.append(words[i])
        
        return len(res)