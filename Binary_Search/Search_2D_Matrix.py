class Solution:
    # strat : isolate the row in the matrix which contains the target
    # than run binary search on that row which is O(logn time)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        targetRow = []
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            middle = l + ((r - l) // 2)
            
            if target < matrix[middle][0]:
                r = middle - 1
            elif target > matrix[middle][-1]:
                l = middle + 1
            else:
                targetRow = matrix[middle]
                break
        
        def binarySearch(row):
            left, right = 0, len(row) - 1
            
            while left <= right:
                middle = left + ((right - left) // 2)
                
                if row[middle] > target:
                    right = middle - 1
                elif row[middle] < target:
                    left = middle + 1
                else:
                    return True
            return False
        
        return binarySearch(targetRow)

