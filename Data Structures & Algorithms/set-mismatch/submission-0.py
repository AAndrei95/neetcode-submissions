from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing_num = list(set([x for x in range(1, n+1)]) - set(nums))
        duplicate = Counter(nums).most_common(1)[0][0]
        
        return [duplicate, missing_num[0]]

    
       

        



        