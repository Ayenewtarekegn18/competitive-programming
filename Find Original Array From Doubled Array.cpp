class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
    vector<int> check;
       sort(changed.begin(),changed.end());
        
        if (changed.size()==1)
        return check;
        if(changed.size()%2!=0)
         return check;
queue <int> mp;
int y=changed.size();
    for(int i=0;i<changed.size();i++)
    { 
        if (mp.empty())
            mp.push(changed[i]);             
        else 
        {
            if (mp.front()*2==changed[i])
                {
                 check.push_back(mp.front());
                  mp.pop();   
                }
            else
                 mp.push(changed[i]);
                
        }
    } 
    double z=y/2;
    if (check.size()==z)
        return check;
    else 
        return vector <int> {}; 
    }
};
