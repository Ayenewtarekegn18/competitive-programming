class Solution {
public:
    string removeStars(string s) {
        string ans;
        for (int i=0;i<s.size();i++){
            if (s[i]=='*' && !s.empty()){
            ans.pop_back();
            continue;
            }
            else
            ans.push_back(s[i]);
        }
        return ans;
    }
};
