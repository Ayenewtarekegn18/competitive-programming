 
class Solution {
public:
vector<int> ans;

    bool findTarget(TreeNode* root, int k) {
        traverse(root,k);
        int i=0,j=ans.size()-1,z=0;
        sort(ans.begin(),ans.end());
        while(i < j)
        {
            if(ans[i]+ans[j]==k){
            z++;
            break;
            }
            else if((ans[i]+ans[j])>k)
            j--;
            else
            i++;

        }
     return z!=0;
    }
   void traverse(TreeNode *root,int k){
        if(root==NULL)
        return;
        ans.push_back(root->val);
        traverse(root->left,k);
        traverse(root->right,k);

    }
};
