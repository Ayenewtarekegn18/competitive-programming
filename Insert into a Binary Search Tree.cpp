class Solution {
public:
int i=0;
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* temp=root;
        if (root==NULL){
        TreeNode* insert=new TreeNode(val);
        root=insert;
        }
        else
        traverse(temp,val);
        return root;
        
    }
    void traverse(TreeNode* temp, int val){
        if (temp==NULL){
            i--;
            return;
        }
        if(val>temp->val)
        traverse(temp->right,val);
        else
        traverse(temp->left,val);
        if(i!=0){
        TreeNode* insert=new TreeNode(val);
        if(val>temp->val)
        temp->right=insert;
        else
        temp->left=insert;
        i=0;
        }


    }
};
