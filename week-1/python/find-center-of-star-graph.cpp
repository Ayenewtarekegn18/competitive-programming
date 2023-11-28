class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int num,num1,cnt1=0,cnt2=0;
            int n=edges.size();
            num=edges[0][0];
            num1=edges[0][1];
                        
            if (num==edges[n-1][0] || num==edges[n-1][1]){
                cnt1++;
            }
            else 
            cnt2++;

        if (cnt1==1)
        return num;
        else 
        return num1;
            }
};