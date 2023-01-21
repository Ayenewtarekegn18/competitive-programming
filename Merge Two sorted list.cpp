class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head1=list1;
         ListNode* head2=list2;
         ListNode* temp;
        if(head1==NULL)
             return head2;
         if(head2==NULL)
             return head1;
    
        temp=head1;

       if(head1->val>head2->val){
            temp=head2;
            head2=head2->next;
           }
        else {
            head1=head1->next;
           }

        ListNode* answer=temp;
      while (head1 && head2)
      { 
        if(head1->val<head2->val){
            answer->next=head1;
            head1=head1->next;
           }
        else{
            answer->next=head2;
            head2=head2->next;
           }
        answer=answer->next;
      }
       if(!head1)
            answer -> next = head2;
        else
            answer -> next = head1;
      return temp;    
    }
};
