class Solution:
    def countSubstr (self, s, k):
        # your code here
        def atmost(s,k):
            freq = {}
            left = 0
            count = 0
            
            for right in range(len(s)):
                
                if s[right] not in freq:
                    freq[s[right]] = 0
                    k -= 1
                
                freq[s[right]] += 1
                
                while k < 0:
                    freq[s[left]] -= 1
                    
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                        k += 1
                    
                    left += 1
                
                count += right - left + 1
                
            return count
        
        return atmost(s,k) - atmost(s, k - 1)
                
        
        return result
