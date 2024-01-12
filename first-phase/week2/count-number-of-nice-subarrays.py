class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        res = 0 
        count = 0
        odd_count = 0
        result = 0
        for elements in nums:
            if elements % 2 == 1: 
                odd_count +=1
                count = 0
            while odd_count == k:
                if nums[i] %2 == 1:
                    odd_count -=1
                i+=1
                count+=1
            result+=count
        return result
                


