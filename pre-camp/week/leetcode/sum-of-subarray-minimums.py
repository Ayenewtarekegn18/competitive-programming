class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def compare(nums,flag):
            stack = []
            ans = [0]* len(nums)
            nums.append(-inf)
            for i in range(len(nums)):

                while stack and (nums[i] < nums[stack[-1]]  or (flag and nums[i] == nums[stack[-1]])):
                     
                    x = stack.pop()
                    ans[x] = i - x
                stack.append(i)

            return ans
        left = compare(arr,False)
        right = compare(arr[::-1],True)[::-1]

        result = 0

        for i in range(len(arr) - 1):
            result += arr[i] * left[i] * right[i]
        return result % (10**9  + 7)






        

                

        