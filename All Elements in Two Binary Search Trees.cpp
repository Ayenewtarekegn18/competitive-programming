class Solution {
public:
    vector<int> ans;
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        traverse(root1);
        traverse(root2);
        sort(ans.begin(),ans.end());
        return ans;
    }
    void traverse(TreeNode* root){
        if(root==NULL)
        return;
        traverse(root->right);
        ans.push_back(root->val);
        traverse(root->left);
        

    }

};
