# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        # maximum = 0
        # count = 1
        # num = arr[0]
        # i = 0
        # j = 1
        # while (i < len(arr)-1) and (j < len(arr)):
        #     if num + arr[j] == k:
        #         maximum = max(count, maximum)
        #         count = 0
        #         num = 0
        #         i+=1
        #         num = arr[i]
            
        #     num += arr[j]
        #     count+=1
        #     j+=1
            
            
        # return maximum
        # left = 0
        # sumation = arr[0]
        # maximum = 0
        
        # for right in range(len(arr)):
        #     if right < len(arr): sumation+= arr[right]
        #     while left <= right and sumation > k:
        #         sumation -= arr[left]
        #         left+=1
                
        #     if sumation == k:
        #         maximum = max(maximum, (right - left) + 1)
                
            
            
            
        
        # return maximum
        summation = 0
        prefix_sum = {}
        max_len = 0
        
        for i in range(len(arr)):
            summation += arr[i]
            
            if summation == k:
                max_len = max(max_len, i + 1)

            
            rem = summation - k
            
            if rem in prefix_sum:
                max_len = max(max_len, i - prefix_sum[rem])
                
            
            if summation not in prefix_sum:
                prefix_sum[summation] = i
                
        
        return max_len

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends