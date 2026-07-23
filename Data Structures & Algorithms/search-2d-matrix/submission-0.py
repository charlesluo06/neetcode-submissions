class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) # number of rows
        cols = len(matrix[0]) # length of the first row (cols)

        #ptrs
        top = 0
        bottom = rows - 1

        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]: #looking at right most val in row
                top = midRow + 1    #shift the range, everything above does not matter
            elif target < matrix[midRow][0]: #looking at left most val in row
                bottom = midRow - 1
            else:   #case if mid is in correct row
                break
        
        if not (top <= bottom): #didnt find the target row
            return False

        row = (top + bottom) // 2
        l = 0
        r = cols - 1

        while l <= r:
            mid = (l+r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False #didnt find target val
        

