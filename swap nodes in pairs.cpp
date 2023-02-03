class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
    
        if (head==NULL)
        return NULL;
        if(head->next==NULL)
        return head;

        ListNode * temp=head;
        ListNode * point=head->next;
        ListNode * begin=head;

         head=point;
         temp->next=point->next;
         point->next=temp;

        while (temp->next!=NULL && point->next!=NULL)
         {
        begin=temp;
        temp=temp->next;
        point=temp->next;
        if(point==NULL)
        return head;
         begin->next=point;
        temp->next=point->next;
        point->next=temp;
         
         }
        return head;
    }
};
