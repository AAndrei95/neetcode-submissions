from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = []

        for i in range(n):
            for j in range(n):
                arr.append(grid[i][j])
        
        arr.sort()

        return [
            Counter(arr).most_common(1)[0][0],
            (set([x for x in range(1, (n*n)+1)]) - set(arr)).pop()
            ]




            
