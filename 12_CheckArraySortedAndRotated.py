class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # Edge case for lenght 1
        # if n == 1: return True
        
        count = 1
        for i in range(1, 2*n):
            if nums[(i -1) % n] <= nums[i % n]:
                count += 1
            else:
                count = 1
        
            if count == n:
                return True
        
        # Edgecase
        # return False 
        return n == 1