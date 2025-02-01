class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i,j,k = 0,1,0
        result = [0] * len(nums)

        for k in range(len(nums)):
            if nums[k] > 0:
                result[i] = nums[k]
                i+=2
            else:
                result[j] = nums[k]
                j+=2

        return result
        # pos, neg = [],[]

        # for i in nums:
        #     if i > 0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)

        # i = 0
        # while 2*i < len(nums):
        #     nums[2*i] = pos[i]
        #     nums[2*i+1] = neg[i]
        #     i+=1

        # return nums

        