class Solution:
    # Recursion
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        result = 0

        if not s: 
            return result

        sign = 1
        i = 0

        if s[i] == '+': 
            i += 1
        elif s[i] == '-': 
            sign = -1
            i += 1

        def helper(s, i, result):
            if i >= len(s) or not s[i].isdigit():
                return result
            
            result = result * 10 + int(s[i])
            return helper(s, i+1, result)
        
        result = helper(s, i, result) * sign

        if result > (2**31) - 1:
            return (2**31) - 1
        elif result < -2**31:
            return -2**31
        else:
            return result
            
    # Using Loop
    # def myAtoi(self, s: str) -> int:
    #     s = s.lstrip()
    #     result = 0

    #     if not s:
    #         return result
        
    #     i = 0

    #     sign = 1

    #     if s[i] == '+':
    #         i += 1
    #     elif s[i] == '-':
    #         sign = -1
    #         i += 1
        
    #     while i < len(s):
    #         curr = s[i]

    #         if not curr.isdigit():
    #             break
    #         else:
    #             result = result * 10 + int(curr)
            
    #         i += 1

    #     result *= sign
        
    #     if result > 2**31 - 1:
    #         return 2**31 - 1
    #     elif result <= -2**31:
    #         return -2**31
    #     else:
    #         return result