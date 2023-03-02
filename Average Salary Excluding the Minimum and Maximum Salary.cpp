class Solution {
public:
    double average(vector<int>& salary) {
        int i=1;
        int n=salary.size()-2;
        double sums=0;
        sort(salary.begin(),salary.end());
        while( i<=n){
        sums=sums+salary[i];
        ++i;
        }
        return sums/n;


    }
};
