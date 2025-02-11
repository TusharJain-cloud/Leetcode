
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        for num in arr:
            if k == num:
                return True
                break
        
        return False
