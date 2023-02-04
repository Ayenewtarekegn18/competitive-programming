class Solution {
public:
    ListNode* sortList(ListNode* head) {
        vector<int> num;
        ListNode *temp=head;
        int count=0;
         if (head==NULL || head->next==NULL)
         {
            return head;
         }
     while(temp!=NULL){
            num.push_back(temp->val); 
            temp=temp->next; 
        }
        temp=head;
        sort(num.begin(),num.end());
        for(int i=0;i<num.size();i++){
            temp->val=num[i];
            temp=temp->next;
        }
         return  head;
    }
};
