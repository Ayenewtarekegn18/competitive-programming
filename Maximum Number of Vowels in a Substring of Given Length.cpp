class Solution {
public:
    int maxVowels(string s, int k) {
        int maximum=0;
        deque<int>q;
        for(int i=0;i<k;i++){
            if(s[i]=='a' || s[i]=='e' ||s[i]=='i' || s[i]=='o' || s[i]=='u'){
                q.push_back(i);
            }
             
        }
        int num=q.size();
        maximum=max(num,maximum);
        for(int i=k;i<s.size();i++){
            if(!q.empty() && i-q.front()>=k){
                q.pop_front();
            }
            if(s[i]=='a' || s[i]=='e' ||s[i]=='i' || s[i]=='o' || s[i]=='u'){
                q.push_back(i);
            }
        
              int num=q.size();
             maximum=max(num,maximum);
            
            
        }
        return maximum;
    }
};
