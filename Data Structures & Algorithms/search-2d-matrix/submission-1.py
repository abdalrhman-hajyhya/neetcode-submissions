class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        targetRow = -1
        rowLeft = 0
        rowRight = rows - 1

        while rowLeft <= rowRight:
            mid = (rowRight + rowLeft) // 2

            if matrix[mid][0] > target:
                rowRight = mid - 1
            elif matrix[mid][0] < target:
                if matrix[mid][cols - 1] > target:
                    targetRow = mid
                    break
                elif matrix[mid][cols - 1] < target:
                    rowLeft = mid + 1
                else:
                    return True
            else:
                return True
        
        if targetRow == -1:
            return False
        
        colLeft = 0
        colRight = cols - 1
        
        while colLeft <= colRight:
            mid = (colLeft + colRight) // 2

            if matrix[targetRow][mid] > target:
                colRight = mid - 1
            elif matrix[targetRow][mid] < target:
                colLeft = mid + 1
            else:
                return True
        
        return False
        