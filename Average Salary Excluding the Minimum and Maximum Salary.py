class Solution:
    def average(self, salary: List[int]) -> float:
        i=1
        sums=0
        n=len(salary)-1
        salary.sort(reverse=True)  
        while i < n:
            sums=sums+salary[i]
            i=i+1
        return sums/(n-1)
