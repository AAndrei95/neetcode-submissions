class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = 0
        arr_set = set(arr)

        for num in arr:
            if num+1 in arr_set:
                cnt += 1
                
        return cnt


        