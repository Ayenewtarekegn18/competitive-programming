class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector <int> ans;
        for(int i=0;i<nums.size();i++){
            if (i==0)
            ans.push_back(nums.at(i));
            else{
                ans.push_back(ans.at(i-1)+nums.at(i));
            }      
        }
        return ans;
    }
};
