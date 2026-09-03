class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for side, amount in shift:
            amount %= len(s)
            if side == 0:
                s = s[amount:] + s[:amount]
            else:
                s = s[-amount:] + s[:-amount]
            
        return s





        