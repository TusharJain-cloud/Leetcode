from typing import List

class Solution:
    
    def insert(self, St, val):
        if not St:
            St.append(val)
            return
            
        
        temp = St.pop()
        self.insert(St, val)
        St.append(temp)
        
    def reverse(self,St): 
        #code here
        if len(St) == 1:
            return St
        
        temp = St.pop()
        self.reverse(St)
        self.insert(St, temp)