class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(nums[l], result)
                break

            mid = l + ((r-l)//2)
            result = min(nums[mid], result)

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:   
                r = mid - 1            

        return result

        