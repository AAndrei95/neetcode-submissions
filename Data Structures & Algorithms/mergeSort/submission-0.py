# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        mid = len(pairs) // 2
        left_half = pairs[:mid]
        right_half = pairs[mid:]

        sortedLeft = self.mergeSort(left_half)
        sortedRight = self.mergeSort(right_half)

        return self.merge(sortedLeft, sortedRight)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result
