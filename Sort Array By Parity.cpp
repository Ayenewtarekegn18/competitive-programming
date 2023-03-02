class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
          int i=nums.size()-1;
          int j=0;
        while(j < i)
        {
              if ( nums.at(j) % 2!=0) 
              {
                    swap(nums.at(j),nums.at(i));
                       --i;
              }
              else 
              j++;
        }
        
              return nums;
    }
};
