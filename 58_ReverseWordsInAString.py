class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        words = s.split()

        for i in range(len(words) - 1, -1, -1):
            result.append(words[i])
            if i != 0:
                result.append(" ")
        
        return "".join(result)


        