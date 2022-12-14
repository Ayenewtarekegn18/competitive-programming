class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
     ListNode* another=head;
     if(head!=NULL) {
       while( another->next!=NULL){
         if (another->val==another->next->val) 
         {
             another->next=another->next->next;
             
         }
         else
         another=another->next;
       }
     }
    return head;
}
    
};
