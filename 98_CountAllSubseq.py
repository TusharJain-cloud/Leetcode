#Subsequence with target sum
class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        res = 0

        def backtrack(i, cur_sum):
            nonlocal res
            if cur_sum == k:
                res += 1
                return 

            if i == len(nums):
                return
            
            backtrack(i + 1, cur_sum + nums[i])
            backtrack(i + 1, cur_sum)
        
        backtrack(0,0)
        return res
                