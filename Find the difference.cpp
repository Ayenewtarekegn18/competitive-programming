class Solution {
public:
    char findTheDifference(string s, string t) {
        stack <char> dif;
        char y;
      
        for (auto c:t)
        {
            if (!dif.empty())
            break;
            dif.push(c);
            for (int i=0;i<s.length();i++)
            {
                if (dif.top()==s[i])
                {
                s.erase(s.begin() + i);
                dif.pop();
                break;
                }

            }
        }
        return dif.top();
        }
       
};
