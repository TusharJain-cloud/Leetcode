class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summation = 0
        prefix_sum = {0:1}
        for i in range(len(nums)):
            summation += nums[i]
            rem = summation - k
            count += prefix_sum.get(rem, 0)
            prefix_sum[summation] = 1 + prefix_sum.get(summation, 0)

        return count