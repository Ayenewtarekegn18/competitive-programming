class Solution {
public:    
     int pos=0;
    string decodeString(string s)
     {
         int len=s.length();
         string ans="";

        while (pos<len)
        {
            int k;
            string subs="";
            if (s[pos]==']')
            {
            pos++;
            return ans;
            }
            while (pos<len && '0'<=s[pos] && s[pos]<='9')
            {
                k = k*10+s[pos]-'0';
                pos++;

            }
            if (s[pos]=='['){
                pos++;
                subs=decodeString(s);
            }
            while(k){
                ans=ans+subs;
                k--;
            }
            while(pos<len && 'a'<=s[pos] && s[pos]<='z')
            {
                ans.push_back(s[pos]);
                pos++;
            }
        }
        return ans;
    }
};
