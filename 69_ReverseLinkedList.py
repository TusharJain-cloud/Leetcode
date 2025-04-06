# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        second = head


        while second:
            new_node = second.next
            second.next = first
            first = second
            second = new_node
        
        return first
            
        