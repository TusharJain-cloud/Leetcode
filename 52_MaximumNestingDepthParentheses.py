class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        count = 0

        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            
            result = max(result, count)
        
        return result