class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(numRows - 1):
            tempRow = [0] + triangle[-1] + [0]
            newRow = []
            for j in range(len(triangle[-1]) + 1):
                newRow.append(tempRow[j] + tempRow[j+1])
            triangle.append(newRow)

        return triangle

                
