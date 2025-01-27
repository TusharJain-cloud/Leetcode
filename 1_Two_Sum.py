#time complexity: O(n)
#space complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        length = len(nums)
        for i in range(length):
            curr = nums[i]
            diff = target - curr
            if diff in dict and i != dict[diff]:
                return [i,dict[diff]]
            dict[curr] = i
        return [-1,-1]