class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        curr = len(nums)-1
        print(nums)
        while curr >= 2:
            l = 0
            r = curr-1
            while r>l:
                if nums[curr] < nums[l] + nums[r]:
                    count += r-l
                    r-=1
                else:
                    l += 1
            curr -=1
        return count
