'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head is None:
            return None
            
        current = head
        
        while current:
            
            current.next, current.prev = current.prev, current.next
            
            head = current
            current = current.prev
            
        
        return head
        