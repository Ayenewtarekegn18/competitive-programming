class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
     int n = nums.size();
        unordered_set<int> check;
        int cur_sum = 0,prev_sum = 0,mod;
        for(int i = 0; i < n; i++)
        {
            cur_sum+=nums[i];
            mod = cur_sum%k;
            if(check.count(mod) > 0)
            {
                return true;     
            }
            check.insert(prev_sum);
            prev_sum = mod;
        }
        return false;   
    }
};
