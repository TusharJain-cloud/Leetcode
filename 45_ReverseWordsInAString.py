class Solution:
    def reverseWords(self, s: str) -> str:
       s_upd = s.strip()
       s_list = s_upd.split()

       
       result = s_list[::-1]

       return " ".join(result)