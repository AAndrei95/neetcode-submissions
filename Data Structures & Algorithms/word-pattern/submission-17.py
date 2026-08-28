class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        matching_pairs = {}
        matching_pairs_rev = {}

        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in matching_pairs:
                if s[i] in matching_pairs_rev:
                    return False
                matching_pairs[pattern[i]] = s[i]
                matching_pairs_rev[s[i]] = pattern[i]
            else:
                if matching_pairs[pattern[i]] != s[i]:
                    return False
            
        return True
        