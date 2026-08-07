class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key = {}
        dist = 0

        for i in range(len(keyboard)):
            key[keyboard[i]] = i
        
        for j in range(len(word)):
            if j > 0:
                dist = dist + abs(key[word[j]] - key[word[j-1]])
            else:
                dist = key[word[j]]
        
        return dist
            
