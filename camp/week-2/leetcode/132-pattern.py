class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        currMin = -inf
        stack = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < currMin:
                return True
            while stack and stack[-1] < nums[i]:
                currMin = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False

