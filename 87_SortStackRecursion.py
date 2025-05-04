class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    
    def insert(self, s, element):
        if not s or s[-1] <= element:
            s.append(element)
            return
        
        top = s.pop()
        self.insert(s, element)
        s.append(top)
    
    def Sorted(self, s):
        # Code here
        if not s:
            return
        
        top = s.pop()
        self.Sorted(s)
        
        self.insert(s, top)
