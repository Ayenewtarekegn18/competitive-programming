class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # freq = {}
        # for i in arr:
        #     if i in freq:
        #         freq[i] +=1
        #     else:
        #         freq[i] = 1

        # x = ceil(25*len(arr)/100)
        # ans = 0
        # ans1 = 0
        # for key,val in freq.items():
        #     if val >=x:
        #         if val > ans:
        #             ans1 = key  
        # return ans1 
        x = Counter(arr)
        freq = x.most_common()
        return freq[0][0]
        
