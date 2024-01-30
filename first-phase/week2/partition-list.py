# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallHead = ListNode()
        smallPointer = smallHead
        largeHead = ListNode()
        largePointer =  largeHead
        while head:
            if head.val >= x:
                largePointer.next = head
                largePointer= largePointer.next
                
            else:
                smallPointer.next = head
                smallPointer= smallPointer.next
            
            head = head.next
        smallPointer.next = largeHead.next
        largePointer.next = None
        return smallHead.next
