class Solution {
public:
    int fib(int n) {
        int t0=0;
        int t1=1;
        int t2=1;   
        int next=0;
   // for initial values 
        if(n == 1) 
            return t1 ;
        if(n == 2) 
            return t2;
// loop to iterate the adition of the last two values
     for(int i=1;i<n;i++){
        next= t0 + t1;
        t0 = t1;
        t1 = next;
        }
    return next;

    }
};
