class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here
        # a = set(a)
        # b = set(b)
        
        # c = a.union(b)
        # d = list(c)
        # d.sort()
        
        # return d
        result = []
        m = len(a)
        n = len(b)
        
        i = 0
        j = 0
        
        while i < m and j < n:
            if a[i] <= b[j]:
                if len(result) == 0 or a[i] != result[-1]:
                    result.append(a[i])
                    
                i += 1
            else:
                if len(result) == 0 or b[j] != result[-1]:
                    result.append(b[j])
                    
                j += 1
        

        while i < m:
            if a[i] != result[-1]:
                result.append(a[i])
                    
            i += 1
            
        while j < n:
            if b[j] != result[-1]:
                result.append(b[j])
                    
            j += 1
            
        return result