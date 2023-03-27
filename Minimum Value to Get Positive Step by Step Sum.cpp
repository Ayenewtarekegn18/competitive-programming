class Solution {
public:
    int minStartValue(vector<int>& vec) {
        int value = 1;
        int sum = 1;
        for(int i=0;i<vec.size();i++) {
           sum += vec[i];
           if(sum < 1) {
               value++;
               sum = value;
               i = -1;
           }
        }
        return value;
    }
};
