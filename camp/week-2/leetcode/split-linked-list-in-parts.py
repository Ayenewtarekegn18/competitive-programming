# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        N = 0
        while temp:
            temp = temp.next
            N+=1
        ans = []
        count=0
        curr=head

        while(k>0):
            sublist=ceil((N-count)/k)
            if sublist==0:
                ans.append(None)
            else:
                ans.append(curr)
                prev=curr
                while(sublist>0 and curr):
                    prev=curr
                    curr=curr.next
                    count+=1
                    sublist-=1
                prev.next=None
            k-=1
            
        return ans



