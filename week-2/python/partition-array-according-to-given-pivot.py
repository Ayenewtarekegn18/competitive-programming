class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan = []
        greaterthan = []
        equal = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                greaterthan.append(nums[i])
            elif nums[i] < pivot:
                lessthan.append(nums[i])
            else:
                equal.append(nums[i])
        return lessthan + equal + greaterthan
       
        
        
