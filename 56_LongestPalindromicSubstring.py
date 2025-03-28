class Solution:      
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for i in range(len(s)):
            # For odd
            l, r = i, i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result = s[l:r+1]
                    result_len = r - l + 1
                
                l -= 1
                r += 1
            
            # For even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result = s[l:r+1]
                    result_len = r - l + 1
                
                l -= 1
                r += 1
        
        return result
    
    
    # Brute Force
    # TC --> O(n^3)
    # def reverseString(self, s):
    #     return s[::-1]
    
    # def longestPalindrome(self, s: str) -> str:
    #     result = ""
    #     for i in range(len(s)):
    #         substr = ""

    #         for j in range(i, len(s)):
    #             substr += s[j]
    #             reveStr = self.reverseString(substr)
    #             if substr == reveStr:
    #                 if len(substr) > len(result):
    #                     result = substr
                    
    #             continue
        
    #     return result

                

        