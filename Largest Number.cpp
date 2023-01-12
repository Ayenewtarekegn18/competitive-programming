class Solution {
public:
    static bool comp(string &a, string &b){
        return a + b > b + a;
    } 

    string largestNumber(vector<int>& nums) {
        int n = nums.size();
        string large = "";
        vector<string> str;
        int x=0;
        for(int i = 0; i < n; i++){
            if (nums.at(i)==0)
                x++;
            str.push_back(to_string(nums[i]));
        }
        
        sort(str.begin(), str.end(), comp);
        
        for(int i = 0; i < n; i++){
            large += str[i];
        }
        if (x==n){
            return "0";
        }
        else
        return large;
