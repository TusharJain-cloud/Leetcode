class Solution:
    def checkSubsequenceSum(self, nums, k):
        #your code goes here
        def backtrack(i, cur_sum):
            if cur_sum == k:
                return True
            if i == len(nums):
                return False

            if backtrack(i + 1, nums[i] + cur_sum):
                return True
            if backtrack(i + 1, cur_sum):
                return True

            return False
        
        return backtrack(0,0)