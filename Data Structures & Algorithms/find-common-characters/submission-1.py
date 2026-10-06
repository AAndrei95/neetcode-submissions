from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordsCounter = Counter(words[0])
        res = ""

        for i in range(1, len(words)):
            wordsCounter = wordsCounter & Counter(words[i])
        
        for char, freq in wordsCounter.items():
            res += char*freq

        return list(res)