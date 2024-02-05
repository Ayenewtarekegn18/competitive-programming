class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        size_n =len(set(nums))
        i = 0 
        j = 0
        count = 0
        counter = Counter()
        while j <len(nums):
            counter[nums[j]] +=1
            while len(counter) == size_n:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    del counter[nums[i]]
                i+=1
                count += len(nums)-j
            j += 1
        return count
    