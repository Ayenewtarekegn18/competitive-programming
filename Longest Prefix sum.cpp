class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        string f=strs[0],l=strs[strs.size()-1];
        string ans="";
        for(int i=0;i<f.size();i++)
        {
            if(f[i]==l[i])
                ans+=f[i];
            else
                break;
        }
        return ans;
        
    }
};
