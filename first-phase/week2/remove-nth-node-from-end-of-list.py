# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        if head.next == None:
            del head 
            return None

        curr = head 
        while curr:
            count+=1
            curr = curr.next
            
        index = count - n
        curr = head
    
        for i in range(1,index):
            curr = curr.next
        if index == 0:
            head = curr.next
            return head

        if curr.next.next == None:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head
    