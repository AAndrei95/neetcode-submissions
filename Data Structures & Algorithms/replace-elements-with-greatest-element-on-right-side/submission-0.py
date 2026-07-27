class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = 0

        for i in range(len(arr)):
            n = i + 1
            max_num = 0
            while n < len(arr):
                if arr[n] > max_num:
                    max_num = arr[n]
                n += 1
            arr[i] = max_num       
        arr[len(arr)-1] = -1
        return arr
