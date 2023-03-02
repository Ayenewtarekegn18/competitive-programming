class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        set <int> x;
        int count=0;
        for(auto i:arr){
            x.insert(i);
        }
          for(auto i:arr)
          {
          if (i==0)
          count++;
          }
        if (count>=2)
          return true;

        for(auto i:arr){
            if (i!=0 && x.find(i*2)!=x.end())
             return true;
        }
       
        return false;
    }
};
