class Solution {
    static bool comp(pair<int,int>a,pair<int,int>b){
        
        return(a.second>b.second) ;
    }
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        vector<pair<int,int>> store;
        for(auto i: nums)
        ++freq[i];

        for(auto i: freq)
        store.push_back({i.first,i.second});
        sort(store.begin(),store.end(),comp);

        vector<int> ans;
        while(k--){
           ans.push_back(store[k].first) ;
            
        }
        return ans;
        }
};
