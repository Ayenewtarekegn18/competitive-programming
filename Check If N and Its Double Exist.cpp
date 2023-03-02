class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        set <int> x;
        for(auto i:arr)
        {
            x.insert(i);
        }
        for(auto i:arr)
        {
            if (i!=0 && x.find(i*2)!=x.end())
             return true;
        }
       
        return count(arr.begin(),arr.end(),0)>1;
    }
};
