class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        ListNode *temp=head;
        vector<int> ans;
        ListNode *temp2;
        int flag;
        while(temp->next!=NULL)
        {
            temp2=temp->next;
            flag=0;
            while(temp2!=NULL)
            {
            if(temp->val<temp2->val)
            {
            ans.push_back(temp2->val);
            flag++;
            break;
            }
              
        temp2=temp2->next;
             }
             if (flag==0)
            ans.push_back(0);
        temp=temp->next;
        }
        ans.push_back(0);
return ans;
    }
};
