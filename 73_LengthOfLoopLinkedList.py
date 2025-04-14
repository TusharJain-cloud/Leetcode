# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                length = 1

                fast = fast.next

                while fast != slow:
                    length += 1
                    fast = fast.next

                return length

        return 0  