'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        current = head
        
        length = 1
        while current.next:
            current = current.next
            length += 1
            
        return length