'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        head = Node(arr[0])
        current = head
        
        i = 1
        while i < len(arr):
            current.next = Node(arr[i])
            current.next.prev = current
            current = current.next
            i+=1
        
        return head