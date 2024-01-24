# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        nexts= None
        while current is not None:
            nexts = current.next
            current.next = prev
            prev = current
            current = nexts
        head = prev
        return head