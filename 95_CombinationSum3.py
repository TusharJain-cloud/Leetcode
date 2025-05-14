class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(pos, cur, target):
            if target == 0 and len(cur) == k:
                res.append(cur.copy())
            if target <= 0 or len(cur) >= k:
                return

            for i in range(pos, 10):
                cur.append(i)
                backtrack(i + 1, cur, target - i)
                cur.pop()

        backtrack(1, [], n)
        return res