class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size()-1;
       // sort(nums.begin(),nums.end());
        for (int i =0;i<nums.size();i++)
        {
            if (nums.at(i)==val)

             {
             nums.erase(nums.begin()+i);
             --i;  
             }
                
        }
             return nums.size();
    }
   
};
