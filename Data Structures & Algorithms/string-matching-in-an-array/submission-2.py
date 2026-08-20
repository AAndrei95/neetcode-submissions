class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words.sort()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and words[i] not in res and i != j:
                    res.append(words[i])
        
        return res