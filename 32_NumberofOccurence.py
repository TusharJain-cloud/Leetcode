class Solution:
    def countFreq(self, arr, target):
        #code here
        left = self.binSearch(arr, target, True)
        right = self.binSearch(arr, target, False)
        
        if left == -1:
            return 0
            
        
        count = right - left + 1
        return count
        
        
    def binSearch(self, arr, target, leftBias):
        left, right = 0, len(arr) - 1
        i = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target > arr[mid]:
                left = mid + 1
            elif target < arr[mid]:
                right = mid - 1
            else:
                i = mid
                
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return i
    

