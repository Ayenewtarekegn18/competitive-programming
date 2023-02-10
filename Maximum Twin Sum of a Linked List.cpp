class Solution {
public:
    int pairSum(ListNode* head) {
         ListNode *temp=head;
        vector<int> temp1;
       
        int sum=0;
        while (temp!=NULL)
        {
        temp1.push_back(temp->val);
        temp=temp->next;
        } 
         int n=temp1.size();
         int j=0;
        for (int i=0;i<=(n/2)-1;i++)
        { 
            j=(n-1-i);
        
            sum=max((temp1[i]+temp1[j]),sum);
            j--;
        }
      return sum;
        }
};
