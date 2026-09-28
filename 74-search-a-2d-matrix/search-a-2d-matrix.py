class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        end=rows*cols-1
        while start<=end:
            mid = (start+end)//2
            row = mid // cols
            col=mid % cols 
            value = matrix[row][col]
            if value == target:
                return True 
            elif value< target:
                start=mid+1
            else:
                end=mid - 1
        return False