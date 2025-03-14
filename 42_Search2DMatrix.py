class Solution:
    def binSearch(self, arr, target):
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        low = 0
        high = m - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                return self.binSearch(matrix[mid][:], target)
        
        return False
        
        