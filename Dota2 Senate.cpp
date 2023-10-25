class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> d,r;
        int n=senate.length();
        for (int i=0;i<n;i++)
        {
            if (senate[i]=='R')
            r.push(i);
            else
            d.push(i);
        }
        while(!d.empty() && !r.empty())
        {
          if (d.front()>r.front())
            r.push(n++);
            else
            d.push(n++);  
        r.pop(),d.pop();
         }
         return (r.empty())?("Dire"):("Radiant");
    }
};
