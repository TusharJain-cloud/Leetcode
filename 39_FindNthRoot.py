class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
        l, r = 0, m
        result = -1
        
        while l <= r:
            
            mid = l + ((r - l) // 2)\
            
            if mid**n > m:
                r = mid - 1
            elif mid**n < m:
                l = mid + 1
            else:
                result = mid
                break
        
        return result
        