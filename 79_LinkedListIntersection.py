# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # with two pointers
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1

    # With hashmap
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     freq = set()
    #     l1 = headA
    #     l2 = headB

    #     while l1:
    #         freq.add(l1)
    #         l1 = l1.next

    #     while l2:
    #         if l2 in freq:
    #             return l2
            
    #         l2 = l2.next

    #     return None


        