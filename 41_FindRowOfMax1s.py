class Solution:
    def findLowerBound(self, arr, m, x):
        ans = m
        low = 0
        high = m - 1
        
        while low <= high:
            mid = low + ((high - low)//2)
            
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        
    def rowWithMax1s(self, arr):
        # code here
        count_max = 0
        index = -1
        n = len(arr)
        m = len(arr[0])
        
        for i in range(len(arr)):
            count_ones = m - self.findLowerBound(arr[i], m, 1)
            if count_ones > count_max:
                count_max = count_ones
                index = i
            
        return index