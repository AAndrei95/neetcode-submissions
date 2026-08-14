class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = 0
        arr.sort()

        for i in range(len(arr)-1):
            if arr[i]+1 in arr:
                cnt += 1
                
        return cnt


        