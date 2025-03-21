class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {},{}

        for i in range(len(s)):
            val1, val2 = s[i], t[i]

            if (val1 in mapST and val2 != mapST[val1]) or (val2 in mapTS and val1 != mapTS[val2]):
                return False 

            mapST[val1] = val2
            mapTS[val2] = val1 

        return True