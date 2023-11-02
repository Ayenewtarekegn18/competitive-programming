class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
     int n=deck.size()-1;
     vector <int> an;
     deque<int> ans;
     
     sort(deck.begin(),deck.end());
      ans.push_front(deck.back());
      deck.pop_back();
       while (!deck.empty()) 
    {
            ans.push_front(ans.back());
            ans.pop_back();
            ans.push_front(deck.back());
            deck.pop_back();
   
    }  
     
     return vector<int>(ans.begin(), ans.end());
    }
};
