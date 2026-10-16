class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ["a", "e", "o", "u", "i"]
        return "".join([x for x in s if x not in vowels])
