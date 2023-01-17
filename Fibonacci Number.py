class Solution:
    def fib(self, n: int) -> int:   
        t0=0
        t1=1
        t2=1
        next=0
        i=1
        if n==1:
            return t1
        if n==2:
            return t2
        while i < n:
            next=t0+t1
            t0=t1
            t1=next
            i=i+1
        return next
