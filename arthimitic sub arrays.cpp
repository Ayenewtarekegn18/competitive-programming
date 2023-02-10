class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
       vector <int> check;
       vector<bool> ans;
       for(auto i=0,j=0;i<l.size();i++){
           int first=l[i];
           int last=r[i];
           while(first<=last)
           {
           check.push_back(nums[first]);
           ++first;
           }
           sort(begin(check),end(check));
           int d = check[1] - check[0];
           for (j=2; j<check.size(); j++)
           {
            if (check[j] - check[j-1] != d)
                 break;
           }
             ans.push_back(j == check.size());

           check.clear();

       }
       return ans; 
    }
};
