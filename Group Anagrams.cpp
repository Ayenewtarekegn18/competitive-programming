class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       unordered_map<string,vector<string>> mp;
          string temp;
       for (auto a:strs)
       {
          temp=a;
           sort(temp.begin(),temp.end());
           mp[temp].push_back(a);
       }
       vector <vector<string>> ans;
       for (auto b:mp){
           ans.push_back(b.second);
       }
       return ans;
    }
};
