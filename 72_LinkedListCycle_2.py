# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break

        else:
            return None

        pointer = head

        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        
        return pointer
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head 
    #     pos = 0
    #     freq = {}

    #     while current:
    #         if current not in freq:
    #             freq[current] = pos
    #         elif current in freq:
    #             return current

    #         current = current.next
    #         pos += 1
        
    #     return None
        