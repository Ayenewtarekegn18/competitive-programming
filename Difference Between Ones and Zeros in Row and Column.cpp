class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid)
     {
         int n=grid.size(),m=grid[0].size();
        vector<int>row1;
        vector<int>row0;
        vector<int>col1;
        vector<int>col0;
      
        vector<vector<int>> ans;
        int x=0,y=0; 
        for(auto g:grid)
        {
            x=0;y=0;
            for(int i=0;i<m;i++)
            {
                if (g[i]==1)
                x++;
                else
                y++;
            }
        row1.push_back(x);
        row0.push_back(y);
        }
        
        for(int j=0;j<m;j++)
        {
            x=0;y=0; 
            for(int i=0;i<n;i++)
            {
                if (grid[i][j]==1)
                x++;
                else
                y++;
            }
        col1.push_back(x);
        col0.push_back(y);
        }

        
        for(int i=0;i<n;i++){
              vector<int>ans1;
            for(int j=0;j<m;j++){
                int c=0; 
                c+=row1[i]+col1[j]-row0[i]-col0[j];
                ans1.push_back(c);
            }
            ans.push_back(ans1);
        }
        return ans;

    }
};
