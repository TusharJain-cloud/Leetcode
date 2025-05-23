''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        if n == 1 and head.val == key:
            return True
        
        current = head
        
        while current:
            if current.data == key:
                return True
            
            current = current.next
        
            
        return False