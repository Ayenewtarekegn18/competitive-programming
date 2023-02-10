bool has_cycle(SinglyLinkedListNode* head) {
    SinglyLinkedListNode* slow=head;
    SinglyLinkedListNode* fast=head;
     
     if (head==NULL || head->next==NULL)
         return 0;
     else
     {
     while (fast!=0 && fast->next!=NULL)
     {   
         slow=slow->next;
        fast=fast->next->next;
         if (slow==fast)
         return 1;
        
     }
        return 0;
     }
