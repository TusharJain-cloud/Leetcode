class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal
        # n = len(s)

        # for i in range(n):
        #     s = s[1:] + s[0]

        #     if s == goal:
        #         return True
        
        # return False