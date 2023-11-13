class Solution {
public:
    string sortVowels(string s) {
        vector <char> temp;
    
        for (int i=0;i<s.size();i++)
        {
            if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
            temp.push_back(s[i]);
        }
        if (temp.size()==s.length()){
        sort (s.begin(),s.end());
        return s;
        
        }
        sort (temp.begin(),temp.end());
        
        for (int i=0;i<s.size();i++)
        {
            if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U' && !temp.empty())
            {
                s[i]=temp[0];
                temp.erase(temp.begin());
            }
        }
        return s;
    }
};
