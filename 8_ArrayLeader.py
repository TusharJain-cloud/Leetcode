class Solution:
    def leaders(self, arr):
        # code here
        leaders = []
        maximum = arr[-1]
        leaders.append(maximum)
        
        for num in range(len(arr)-2,-1,-1):
            if arr[num] > maximum:
                leaders.append(arr[num])
                maximum = arr[num]
                
        
        return leaders.sort()