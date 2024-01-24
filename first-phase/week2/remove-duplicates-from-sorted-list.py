# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        left = head
        right = head.next                                      
        while right and left:
            if right.val != left.val:
                left.next = right
                left = left.next
            right = right.next
        if left:
            left.next = None
        return head