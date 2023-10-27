class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
    int n=nums.size();
    int totalsum=accumulate(nums.begin(),nums.end(),0);
    int target=totalsum-x;
    if (target<0)
    return -1;
    if (target==0)
    return n;

    int count=INT_MAX;
    int csum=0;
    int i=0,j=0;
    while(j<n){
        csum+=nums[j];
        j++;
        while (csum >target && i<n)
        {
            csum-=nums[i];
            i++;
        }
        if (csum==target)
        count=min(count,n-(j-i));

    }
    return count==INT_MAX?-1:count;

    }
};
