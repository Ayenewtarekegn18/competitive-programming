class Solution {
public:
    void rotate(vector<int>& nums, int k) {
         k%=nums.size();
        vector <int> rotate;
        int n= nums.size()-k;
      
        for (int i=n;i<nums.size();i++)
        
            rotate.push_back(nums.at(i));
        }
        for (int i=0;i<n;i++)
        {
             rotate.push_back(nums.at(i));
         }
     nums=rotate;
    
    }
};
