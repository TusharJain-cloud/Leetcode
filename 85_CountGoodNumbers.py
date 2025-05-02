class Solution:
    # def countGoodNumbers(self, n: int) -> int:
    #     MOD = 10 ** 9 + 7
        
    #     def pow(x,n):
    #         if x == 0: return 1
    #         if n == 0: return 1

    #         res = pow(x, n // 2)
    #         res = (res * res) % MOD
            
    #         return ((x*res) % MOD) if n % 2 != 0 else res 

    #     even = ceil(n/2)
    #     odd = n // 2

    #     return (pow(5, even) * pow(4, odd)) % MOD

    # Iterative
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def pow(x,n):
            res = 1
            while n > 0:
                if n % 2:
                    res = (res*x) % MOD
            
                n = n // 2
                x = (x * x) % MOD
            
            return res

        even = ceil(n/2)
        odd = n // 2

        return (pow(5, even) * pow(4, odd)) % MOD
        