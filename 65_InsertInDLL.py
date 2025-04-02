'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
        new_node = Node(x)
        
        current = head
        
        for _ in range(p):
            current = current.next
        
        new_node.next = current.next 
        new_node.prev = current
        current.next = new_node
        
        if new_node.next:
            new_node.next.prev = new_node
            
        return head
        