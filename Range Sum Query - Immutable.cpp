class NumArray {
public:
vector<int>nums;
vector<int>prefix;

    NumArray(vector<int>& nums) {
        this->nums=nums;
        int n=nums.size();
        prefix.resize(n);
        prefixcal(nums);

    }
    
    int sumRange(int left, int right) {
        // return accumulate(this->nums.begin()+left,this->nums.begin()+right+1,0);
      return left-1>=0?prefix[right]-prefix[left-1]:prefix[right];  
    }
    void prefixcal(vector<int>nums){
    for(int i=0;i<nums.size();i++){
        (i==0)?prefix[i]=nums[i]:prefix[i]=prefix[i-1]+nums[i];
    }
    }
};
