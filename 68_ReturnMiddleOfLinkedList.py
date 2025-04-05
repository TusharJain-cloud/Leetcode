import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         length = 1

#         while current:
#             current = current.next
#             length += 1
        
#         i = 1
#         middle_pos = math.ceil(length/2)
#         optional = head
#         while i < middle_pos:
#             optional = optional.next
#             i+=1
        
#         return optional
        