
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        # code here
        i = 1
        n = len(arr)
        
        head = Node(arr[0])
        nextptr = head

        
        while i < n :
            nextptr.next = Node(arr[i])
            nextptr = nextptr.next
            
            i+=1
        
        return head