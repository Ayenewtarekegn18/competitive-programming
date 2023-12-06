class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num=[]
        arr = {}
        for i in nums:
            if i not in arr:
                arr[i] = 1
            else:
                arr[i]+=1
        for key,value in arr.items():
            if value > len(nums)/3:
                num.append(key)
        return num

