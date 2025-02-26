class Solution:
    def findKRotation(self, arr):
        # code here
        result = arr[0]
        index = 0
        l,r = 0, len(arr) - 1
        
        while l <= r:
            
            if arr[l] < arr[r]:
                if result > arr[l]:
                    index = l
                    result = arr[l]
                    break
            
            mid = l + ((r-l) // 2)
            if result > arr[mid]:
                result = arr[mid]
                index = mid
            elif arr[l] <= arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return index