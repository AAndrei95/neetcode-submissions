from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        wordsCounter = Counter()

        for word in words:
            wordsCounter += Counter(word)   

        for char, freq in wordsCounter.items():
            if freq % len(words) != 0:
                return False

        return True
        
        