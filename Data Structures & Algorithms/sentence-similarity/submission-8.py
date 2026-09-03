class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        unique_pairs = set()

        for a, b in similarPairs:
            unique_pairs.add((a, b))
            unique_pairs.add((b, a)) 

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            if (word1, word2) not in unique_pairs:
                return False
        return True        