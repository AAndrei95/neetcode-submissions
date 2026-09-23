from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for i in range(len(words)):
            charsCounter = Counter(chars)
            wordCounter = Counter(words[i])
            cnt = len(words[i])
            for j in range(len(words[i])):
                if words[i][j] not in charsCounter.keys():
                    cnt = 0
                    break
                
                if charsCounter[words[i][j]] == 0:
                    cnt = 0
                    break
                
                charsCounter[words[i][j]] -= 1

            res += cnt

        return res
        