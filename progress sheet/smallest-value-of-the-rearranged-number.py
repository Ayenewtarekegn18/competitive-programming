class Solution:
    def smallestNumber(self, num: int) -> int:
        if  num >= 0:
            nums = [int(digit) for digit in str(num)]
            nums.sort()
            if nums[0] == nums[-1]:
                return num
            else:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        nums[0],nums[i] = nums[i],nums[0]
                        break
                num = ''.join(map(str, nums))
                num= int(num)
                return num
        else:
            num *= -1 
            nums = [int(digit) for digit in str(num)]
            nums= sorted(nums,reverse=True)
            num = ''.join(map(str, nums))
            num= int(num)
            return num*-1
       
       