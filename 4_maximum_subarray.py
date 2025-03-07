# Maximum Subarray Sum
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        maxSum = nums[0]

        for val in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += val
            maxSum = max(maxSum, currSum)

        return maxSum
        