# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        curr = head

        while curr:
            if curr.val == target:
                next_node = curr.next
                prev_node = curr.prev

                if curr == head: head = next_node

                
                if next_node: next_node.prev = prev_node
                
                if prev_node: prev_node.next = next_node
                
                curr = next_node
            else:
                curr = curr.next

        return head 