class Solution(object):
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = -1

        for i in range(len(nums)-2, 0,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        

        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,pivot,-1):
            if nums[i] > nums[pivot]:
               self.swap(nums, i, pivot)
               break
        
        i = pivot + 1
        j = len(nums) - 1
        while i <= j:
            self.swap(nums, i, j)
            i+=1
            j-=1

        return