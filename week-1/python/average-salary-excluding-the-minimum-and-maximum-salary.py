class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        i=1
        j=len(salary)-2
        sum=0
        while(i<=j):
            if i==j:
                sum+=salary[i]
                break
            sum+=salary[i]+salary[j]
            i+=1
            j-=1
        return sum/(len(salary)-2)

