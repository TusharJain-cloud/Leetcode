#Solution for finding kth positive number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,r = 0, len(arr) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            missing = arr[mid] - (mid + 1)

            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        
        '''
        ans = arr[high] + more
        arr[high] + k - missing
        arr[high] + k - (arr[high] - (high + 1))
        arr[high] + k - (arr[high] - high - 1)
        arr[high] + k - arr[high] + high + 1
        high + k + 1 or low + k
        '''
        return l + k
        