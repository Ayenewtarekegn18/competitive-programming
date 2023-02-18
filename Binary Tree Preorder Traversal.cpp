class Solution {
public: 
vector<int> ans;
    vector<int> preorderTraversal(TreeNode* root) {
        traverse(root);
   return ans;
    }
     void traverse(TreeNode* root)
     { 
         if(root==NULL)
          return;
        ans.push_back(root->val);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
     }
};
