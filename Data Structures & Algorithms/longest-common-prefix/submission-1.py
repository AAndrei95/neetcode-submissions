class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]

        for i in range(len(pref)):
            cnt = 0
            for j in range(len(strs)):
                try:
                    if strs[j][i] == pref[i]:
                        cnt += 1
                except:
                    pass
            if cnt < len(strs):
                return pref[:i]
        
        return pref







            