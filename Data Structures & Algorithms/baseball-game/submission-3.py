class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result = []

        for score in operations:
            if score == "+":
                result.append(result[-1] + result[-2])
            elif score == "C":
                result.pop()
            elif score == "D":
                result.append(result[len(result)-1]*2)
            else:
                result.append(int(score))
        
        return sum(result)