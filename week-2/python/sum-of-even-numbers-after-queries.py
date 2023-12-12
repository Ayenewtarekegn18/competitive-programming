class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [] 
        sums = 0
        for i in nums:
            if i%2 == 0:
                sums += i
        for i in queries:
            if nums[i[1]] % 2 == 0:
                sums -= nums[i[1]] 
            nums[i[1]] = nums[i[1]] + i[0]
            if nums[i[1]] % 2 == 0:
                sums += nums[i[1]] 
            ans.append(sums)
        return ans
        
        

