class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
    int counter=0;
    ListNode *temp=head; 
    int x;
    while (temp->next!=NULL)
    {
    counter++;
    temp=temp->next;
    }
    for(int i=1;i<=counter;i++)
    {
        temp=head;
        while (temp->next!=NULL)
        {
           if(temp->val > temp->next->val)
           {
            x=temp->val;
            temp->val=temp->next->val;
            temp->next->val=x;
           }
           temp=temp->next;
        }
    }
    return head;
    }
};
