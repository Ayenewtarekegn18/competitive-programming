class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
ListNode *sums= new ListNode();
    ListNode *temp=sums;
    int n=0;
    while(l1!=NULL || l2!=NULL || n){
        int sum=0;
        if (l1!=NULL){
            sum+=l1->val;
            l1=l1->next;
        }
        if (l2!=NULL){
            sum+=l2->val;
            l2=l2->next;
        }
       sum+=n;
       n=sum/10;
       ListNode * num= new ListNode(sum%10);
       temp->next=num;
       temp=temp->next;

    }

    return sums->next;
    }
};
