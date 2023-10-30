class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
     int n=deck.size();
     vector <int> ans (n);
     queue<int> q;
     sort(deck.begin(),deck.end());
     for (int i=0; i<deck.size();i++)
     {
            q.push(i);
     }  
     for (int i=0;i<n;i++){
         ans[q.front()]=deck[i];
         q.pop();
         if(!q.empty()){
             q.push(q.front());
             q.pop();
         }
     }
     return ans;
    }
};
