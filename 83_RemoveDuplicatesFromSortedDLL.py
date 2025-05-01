# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        curr = head

        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr
            else:
                curr = curr.next
        
        return head