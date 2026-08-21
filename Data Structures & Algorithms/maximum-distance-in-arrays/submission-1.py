class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = []

        for i in range(len(arrays)-1):
            res.append(abs(arrays[i][-1]-arrays[i+1][0]))
            res.append(abs(arrays[i][0]-arrays[i+1][-1]))

        return max(res)