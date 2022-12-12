class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int n=nums.size();
        vector <int> ans;
        int value=0;
      
        for(int i=0;i<n;i++){ 
             for(int j=0;j<n;j++)
             {   
               if(i!=j && nums.at(i)>nums.at(j))
                     value++;
             }
                    ans.push_back(value);
                    value=0;
        }
    return ans;
    }
};
