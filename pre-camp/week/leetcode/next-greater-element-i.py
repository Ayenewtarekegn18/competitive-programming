class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        v = []
        
        for num in nums1:
            j = 0
            
            for j in range(len(nums2)):
                if nums2[j] == num:
                    break
            
            found_greater = False
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums2[j]:
                    v.append(nums2[k])
                    found_greater = True
                    break
            
            if not found_greater:
                v.append(-1)
        
        return v