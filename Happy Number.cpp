class Solution {
public:

        int num(int n){
            long long x=0;
        while (n!=0){
            int temp= n%10;
            x+=temp*temp;
            n=n/10; 
        }
        return x;
        }
    bool isHappy(int n) {
        unordered_set<int>set;
        while(n!=1 && !set.count(n)){
            set.insert(n);
            n=num(n);
        }
        return n==1;
    }
};
