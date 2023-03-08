class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        map<string,int> temp;
        for(auto x:cpdomains)
        {
            int y=x.find(" ");
           int n=stoi(x.substr(0,y));
            string str=x.substr(y+1);
            for (int i=0;i<str.length();i++)
            {
                if(str[i]=='.')
                temp[str.substr(i+1)]+=n;

            }
            temp[str]+=n;
        }
            vector <string> ans;
            for (auto z:temp){
                ans.push_back(to_string(z.second)+" " + z.first);
            }
       return ans; 
    }
};
