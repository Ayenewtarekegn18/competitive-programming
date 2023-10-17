class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        vector<int> avg;
        long long r=k*2+1,sum=0,l=0;


        if (nums.size()>=r)
        {
            for (int i=0;i<k;i++)
                avg.push_back(-1);

            for (int i=0;i<r;i++)
                sum+=nums[i];

            while (r<nums.size())
            {
                avg.push_back(sum/((2*k)+1));
                sum+=nums[r]-nums[l];
                l++;
                r++;
            }
            avg.push_back(sum/((2*k)+1));

        }
        while (nums.size()>avg.size())
        avg.push_back(-1);

        return avg;
    }
};
