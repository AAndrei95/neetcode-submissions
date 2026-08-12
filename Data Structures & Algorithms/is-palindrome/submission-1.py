class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        end = len(s) - 1

        for idx in range(len(s) // 2):
            if s[idx] != s[end-idx]:
                return False
        return True
