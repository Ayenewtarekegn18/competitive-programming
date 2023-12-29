class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = {}
        num2 = {}
        ans = []
        for i in nums1:
            if i in num1:
                num1[i] += 1
            else:
                num1[i] = 1
        for i in nums2:
            if i in num2:
                num2[i] += 1
            else:
                num2[i] = 1
    
        for key,value in num1.items():
            if key in num2:
                n = min(value,num2[key])
                while n != 0:
                    ans.append(key)
                    n -=1
        return ans
