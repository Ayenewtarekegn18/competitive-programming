class Solution {
public:
    int fib(int n) {
        int t0=0,t1=1,t2=1,next=0;
        if(n == 1) 
            return t1 ;
            if(n == 2) 
            return t2;
     for(int i=1;i<n;i++){
        next= t0 + t1;
        t0 = t1;
        t1 = next;
        }
    return next;

    }
};