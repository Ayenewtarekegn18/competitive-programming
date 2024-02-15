class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d1=defaultdict (list)
        for i in range (len(nums)):
            d1[nums[i]].append(i)
        ans=[0]*(len(nums))
        for key,val in d1.items():
            suff=sum(val)
            pre=0
            s=len(val)
            p=0
            for i in val:
                pre+=i 
                p+=1
                suff-=i
                s-=1
                ans[i]=(-pre+p*i-s*i+suff)
        return ans