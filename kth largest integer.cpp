
 bool myCmp(string s1, string s2)
{
    if (s1.size() == s2.size()) 
    {
        return s1 < s2;
    }
    else
    {
        return s1.size() < s2.size();
    }
}
class Solution {
public:
     
    string kthLargestNumber(vector<string>& nums, int k) {
        
    sort(nums.begin(), nums.end(), myCmp);
    for (auto it : nums) {
    }
 

        return nums.at(nums.size()-k);
}
};
