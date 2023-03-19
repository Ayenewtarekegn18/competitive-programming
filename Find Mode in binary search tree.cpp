class Solution {
public:
map<int,int>mp;
    vector<int> findMode(TreeNode* root) {
        TreeNode* temp=root;
        traverse(temp);
        vector<int> ans;
        int max=0;
        map<int, int>::iterator it = mp.begin();

  while (it != mp.end())
  {
            if(it->second>max)
            {
                max=it->second;
                if(ans.empty())
                {
               ans.push_back(it->first);
                }
                else
                {
                while(!ans.empty())
                ans.pop_back();
                ans.push_back(it->first);
                }
                
            }
            else if(it->second==max)
            {
                if(it->first!=ans[ans.size()-1]){
                     ans.push_back(it->first);
                }
            }
            
            ++it;
  }
   
    
        return ans;
    }
     

   void traverse(TreeNode* root)
   {
        if (root==NULL)
        return;
        mp[root->val]++;
        traverse(root->left);
        traverse(root->right);
    }
};
