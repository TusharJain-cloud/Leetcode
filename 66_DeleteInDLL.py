class Solution:
    def delete_node(self, head, x):
        #code here
        if x==1:
            head = head.next
            head.prev = None
            return head


        current = head
        

        for _ in range(1, x - 1):
            current = current.next
            
        
        remove_node = current.next
        current.next = remove_node.next
        
        if remove_node.next:
            remove_node.next.prev = current
        
        
        return head