class Solution:
    def largestGoodInteger(self, num: str) -> str:
        k = 3
        max_int = "000"

        for i in range(0, len(num)-2): 
            if num[i] == num[i+1] == num[i+2]:
                max_int = max(int(max_int), int(num[i]*k))
        
        if int(max_int) > 0:
            return str(max_int)
        elif max_int == 0:
            return "0" * k
        else:
            return ""
        
                

