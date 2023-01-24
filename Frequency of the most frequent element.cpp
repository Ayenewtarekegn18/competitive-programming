class Solution {
public:
    int maxFrequency(vector<int>& nums, long k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int j = 0;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            k =k+ nums[i];

            while(k < (long) nums[i] * (i - j + 1)) {
                k =k- nums[j];
                j++;
            }
            ans = max(ans, i - j + 1);
        }
        return ans;
    }
};
