# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while right:
            if right.val != left.val:
                return False
            
            right = right.next
            left = left.next
        
        return True

        # string = ""
        # current = head
        # string += str(head.val)
        
        # while current.next:
        #     current = current.next
        #     string += str(current.val)    
        
        # reverse_str = string[::-1]
        # if string == reverse_str:
        #     return True
    
        # return False