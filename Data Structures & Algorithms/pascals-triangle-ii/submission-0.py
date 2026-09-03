class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]

        if rowIndex == 0:
            return [1]

        for i in range(rowIndex):
            tempRow = [0] + triangle[-1] + [0]
            newRow = []
            for j in range(len(triangle) + 1):
                newRow.append(tempRow[j] +  tempRow[j+1])
            triangle.append(newRow)
        
        return triangle[-1]