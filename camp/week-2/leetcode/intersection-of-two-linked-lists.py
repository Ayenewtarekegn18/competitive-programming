# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        checker = set()
        node = headB
        while node:
            checker.add(node)
            node = node.next

        node = headA
        while node:
            if node in checker:
                return node
            node= node.next
        return None