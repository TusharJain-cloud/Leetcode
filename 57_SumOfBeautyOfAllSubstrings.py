class Solution:
    # TC --> O(n^2)
    def beautySum(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            freq = [0] * 26

            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('a')

                freq[idx] += 1

                max_freq = max(freq)
                min_freq = min([f for f in freq if f > 0])

                result += max_freq - min_freq

        
        return result


    # TC --> O(n^3)
    # def beautySum(self, s: str) -> int:
    #     count = 0
        
    #     for i in range(len(s) - 1):
    #         for j in range(i+1, len(s)):
    #             substr = s[i:j + 1]
    #             freq = {}
    #             for word in substr:
    #                 if word not in freq:
    #                     freq[word] = 1
    #                 else:
    #                     freq[word] += 1
                
    #             count += max(freq.values()) - min(freq.values()) 

        
    #     return count