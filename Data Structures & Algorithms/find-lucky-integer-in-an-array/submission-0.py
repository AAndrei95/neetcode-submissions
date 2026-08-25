class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = 0
        set_arr = set(arr)

        for num in set_arr:
            if arr.count(num) == num:
                lucky = max(lucky, num)

        if lucky == 0:
            return -1
            
        return lucky


        