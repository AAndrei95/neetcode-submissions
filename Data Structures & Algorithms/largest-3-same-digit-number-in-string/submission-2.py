class Solution:
    def largestGoodInteger(self, num: str) -> str:
        k = 3
        max_int = "0"

        for i in range(len(num)-2): 
            if num[i] == num[i+1] == num[i+2]:
                max_int = max(max_int, num[i]*k)

        return "" if max_int == "0" else max_int
        
        
                

