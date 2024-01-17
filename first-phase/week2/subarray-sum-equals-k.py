class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di = defaultdict(int)
        prefix = 0
        ans = 0
        di[prefix] = 1
        for i in nums:
            prefix += i
            find = prefix - k
            if find in di :
                ans += di[find]
            di[prefix] += 1
        return ans
            
    
           
        return count