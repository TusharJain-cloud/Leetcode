class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def find_sum(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            find_sum(i, cur, total + candidates[i])
            cur.pop()  
            find_sum(i + 1, cur, total)

        find_sum(0, [], 0)  
        return res
        