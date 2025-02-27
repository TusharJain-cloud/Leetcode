class Solution:
    def floorSqrt(self, n): 
    #Your code here
        l, r = 0, n
        result = 0
        
        while l <= r:
            mid = l + ((r - l) // 2)
            
            if mid**2 > n:
                r = mid - 1
            elif mid**2 < n:
                l = mid + 1
                result = mid
            else:
                return mid
        
        return result