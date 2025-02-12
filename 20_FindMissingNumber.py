class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # for i in range(n+1):
        #     if i not in nums:
        #         return i
        summation = (n*(n+1))//2
        sumOfAllElements = sum(nums)
        result =  summation - sumOfAllElements
        return result