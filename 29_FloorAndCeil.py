class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        arr.sort()
        
        maximum = -1
        minimum = -1
        
        low, high = 0, len(arr)-1
        low1, high1 = 0, len(arr)-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                minimum = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        while low1 <= high1:
            mid1 = (low1 + high1) // 2
            
            if arr[mid1] >= x:
                maximum = arr[mid1]
                high1 = mid1 - 1
            else:
                low1 = mid1 + 1
                
        return minimum, maximum