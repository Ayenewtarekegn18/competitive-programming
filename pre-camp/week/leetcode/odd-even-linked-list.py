# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None :
            return head
    
        current_odd = head
        current_even = head.next
        odd = ListNode(0)
        even = ListNode(0)
        odd.next = current_odd
        even.next = current_even

        while current_odd and current_odd.next and current_even and current_even.next:
            current_odd.next = current_odd.next.next
            current_even.next = current_even.next.next
            current_odd = current_odd.next
            current_even = current_even.next
        
        current_odd.next = even.next
        return odd.next