class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0
        for string in s:
            if string == ")": count -= 1
            if count != 0: result += string
            if string == "(": count += 1
        
        return result
