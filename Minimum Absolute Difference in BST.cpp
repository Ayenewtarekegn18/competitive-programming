class Solution {
public:
vector<int> x;
int ans,i=0,j=i+1;
    int getMinimumDifference(TreeNode* root) {
            traverse(root);
            sort(x.begin(),x.end());
            ans=x[j]-x[i];
            while(j<x.size()){
                ans=min(ans,(x[j]-x[i]));
                i++;
                j++;
            }
            return ans;
        
    }
    void traverse (TreeNode* root){
        if(root==NULL)
        return;
        x.push_back(root->val);
        traverse(root->left);
        traverse(root->right);
    }
};
