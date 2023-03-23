class Solution {
public:

    TreeNode* sortedListToBST(ListNode* head) {
        
        vector<int>temp;
        int i,j;
        while(head!=NULL)
        {
            temp.push_back(head->val);
            head=head->next;
        }
        return traverse(temp,0,temp.size()-1);
        
    }

    TreeNode* traverse(vector<int> &temp,int i, int j)
    {

        if(i>j)
        return NULL;

       int mid=i+(j-i)/2;
        TreeNode* root=new TreeNode(temp[mid]);
        root->left= traverse(temp,i,mid-1);
        root->right= traverse(temp,mid+1,j);
        return root;

        }


};
