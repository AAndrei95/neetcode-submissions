class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        res = []
        for query in queries:
            cnt = 0
            for i in range(query[0], query[1]+1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    cnt += 1
            res.append(cnt)

        return res


        