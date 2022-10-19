class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int,int> mp;
        for(auto it:arr){
            mp[it]++;
        }
        
        priority_queue<int> pq;
        
        for(auto it:mp) pq.push(it.second);
        int sum=0;
        int ans=0;
        while(!pq.empty()){
            sum+=pq.top();
            pq.pop();
            ans++;
            if(sum>=(arr.size()/2)) return ans;
        }
        return 0;
    }
};
