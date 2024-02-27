class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono = []
        di = defaultdict(int)
        i = 0
        while i < len(nums2):
                if mono and nums2[i] > mono[-1]:
                    di[mono[-1]] = nums2[i]
                    mono.pop()
                else:   
                    mono.append(nums2[i])
                    i +=1
        for j in range(len(nums1)):
            if nums1[j] in di:
                nums1[j] = di[nums1[j]]
            else:
                nums1[j] = -1

        return nums1
            


