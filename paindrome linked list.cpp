class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode*temp=head;
        vector <int> check;
        while(temp!=NULL)
        {
        check.push_back(temp->val);
        temp=temp->next;
        }
        int i=0,j=check.size()-1;
        while (i<j){
        if (check[i]!=check[j])
         return false;
         i++;
         j--;
        }
        return true;
    }
};
