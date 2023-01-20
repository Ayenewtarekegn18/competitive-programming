class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures)
    {
        stack <pair<int,int>> temp;
        int n=temperatures.size(); 
        vector <int> ans(n);

        for(int i=0;i<n;i++)
        {
            while(!temp.empty() && temp.top().first <temperatures.at(i))
            {
                ans.at(temp.top().second)=i-temp.top().second;
                temp.pop();
            }
            
            temp.push({temperatures.at(i),i});
        }
            while(!temp.empty())
            {
                ans.at(temp.top().second)=0;
                temp.pop();
            }
            return ans;
    }
      
};
