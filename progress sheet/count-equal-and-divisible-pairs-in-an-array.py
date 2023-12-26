class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # mp = defaultdict{}
        # for i in range(len(nums)):
        #     if nums[i] in mp:
        #         mp[nums[i]].append(i)
        #     else:
        #         mp[nums[i]].append(i)
        # for key,value in mp.items():
        #     for i in 
        count = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if j>i and nums[i] == nums[j] and i*j % k == 0:
                    count+=1
        return count
                
                