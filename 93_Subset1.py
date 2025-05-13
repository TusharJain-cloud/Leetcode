class Solution:
    def subsetSums(self, nums):
        #your code goes here
        res = []
        
        def backtrack(i, cur_sum):
            if i == len(nums):
                res.append(cur_sum)
                return
            
            backtrack(i + 1, cur_sum + nums[i])
            backtrack(i + 1, cur_sum)

        backtrack(0, 0)
        return res
