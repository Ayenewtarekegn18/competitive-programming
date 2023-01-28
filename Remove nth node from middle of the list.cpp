class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp=head; 
         int count=0;
         int index;
        while(temp != NULL)
        {
        count +=1;
        temp = temp->next;
         }
         temp=head;
         if (head->next == NULL) {
        delete head;
        return NULL;
         }
         index=count-n;
         for (int i=1;i<index;i++)
         {
          temp=temp->next;
         } 
         if(index==0){
            head=temp->next; 
            return head;
         }
         
         if(temp->next->next==NULL){
             temp->next=NULL;
         }
         else{
          ListNode* copy=temp->next;
          temp->next=copy->next;
          delete copy;
         }
     return head;
     }
        
};
