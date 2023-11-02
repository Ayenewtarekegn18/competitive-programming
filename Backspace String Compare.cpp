class Solution {
public:
    bool backspaceCompare(string s, string t) 
    {
        string s2,t2;
        for (int i=0;i<s.length();i++)
        {
            if (s[i]=='#')
            {
            if (!s2.empty())
            s2.pop_back();
            }
            else
            s2.push_back(s[i]);
        }
        for (int i=0;i<t.length();i++){
            if (t[i]=='#')
             {
            if (!t2.empty())
            t2.pop_back();
            
            }
            else
            t2.push_back(t[i]);
            }
        
        return t2==s2?true:false;
    }
};
