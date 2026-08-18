class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_liters = 0
        i, j = 0, len(heights) - 1

        while i < j:
            max_liters = max(max_liters, ((j-i) * min(heights[i], heights[j])))
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
          
        return max_liters
        