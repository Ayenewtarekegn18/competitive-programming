class Solution {
public:
int i=0,ans=0;
    int kthSmallest(TreeNode* root, int k) {
        traverse(root,k);
        return ans;
    }

   void traverse(TreeNode *root,int k){
        if(root==NULL)
        return;
        traverse(root->left,k); 
         i++;
         if (i==k)
         {
         ans=root->val;
         return;
         }
        traverse(root->right,k);
   }
};
