class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    int i=0;
        for(int j=0;j< nums.size();j++){
              if ( !nums.at(j)==0) 
              {
                    swap (nums.at(i),nums.at(j));
                       i++;
              }
                                  
        }  
    }
      
};
