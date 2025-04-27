# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):
        val = ''

        curr = head
        while curr:
            val += str(curr.val)
            curr = curr.next
        
        # Add one to the integer
        val = str(int(val) + 1)

        # Build the new linked list
        dummy = ListNode()
        curr = dummy
        for digit in val:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
