class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid_nums = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }

        str_n = str(n)
        new_n = []
       
        for num in str_n:
            if int(num) not in valid_nums.keys():
                return False
            elif int(num) in valid_nums.keys():
                new_n.insert(0, valid_nums[int(num)])
        
        return n != int("".join(map(str, new_n)))