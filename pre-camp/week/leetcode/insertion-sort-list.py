# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp.next:
            count+=1
            temp = temp.next
        for i in range(count):
            temp = head 
            while temp.next:
                if temp.val > temp.next.val:
                    x= temp.val
                    temp.val = temp.next.val
                    temp.next.val = x
                temp= temp.next
        return head

