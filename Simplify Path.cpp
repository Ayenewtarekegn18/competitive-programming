class Solution {
public:
    string simplifyPath(string path) {
        vector<string> str;
        string ans;
      
        if (path.length()==1)
            return path;
        
        for (int i=0;i<path.length();i++)
        {
            if (path[i]=='/')
                continue;
            string temp;
            while (i<path.size() && path[i]!='/')
            {
                temp+=path[i];
                ++i;
            }
            if(temp==".")
                continue;
            else if (temp=="..")
            {
                if (!str.empty())
                    str.pop_back();
            }
            else
            str.push_back(temp);

         }
        for (int i=0;i<str.size();i++){
            ans+="/"+str[i];
        }
        if(ans.size() == 0)
            return "/";
        return ans;
    }
};
