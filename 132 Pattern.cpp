class Solution {
public:
    bool find132pattern(vector<int>& nums) {\
        int n=nums.size();
        if (n<=2)
         return false;
        // int i=0,j=2;
        // while(j<n){
        //     if (nums[i]<nums[j] && nums[j]<nums[i+1])
        //     return true;
        //     j++;
        //     i++;
        // }
        // return false;
         int currmin=INT_MIN;
        stack<int> s;
        for (int i=n-1;i>-1;i--)
        {
            if (nums[i]<currmin)
            return true;
            while (!s.empty() && nums[i]>s.top()){
            currmin=s.top();
            s.pop();
            }
           
            s.push(nums[i]);
        
        }
        return false;
    }
};
