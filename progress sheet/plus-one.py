class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for num in digits:
            n = n*10 + num
        n+=1
        ans = []
        while n>0:
            ans.append(n%10)
            n = n//10
        return ans[::-1]
            
            