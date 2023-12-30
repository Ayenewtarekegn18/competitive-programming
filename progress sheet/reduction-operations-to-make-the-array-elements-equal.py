class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(1,50001):
            freq[i] = 0
        for i in nums:
            freq[i] +=1
        arr = []
        ans = 0
        for i in range(1,50001):
            if i in freq:
                if freq[i] > 0:
                    arr.append(i)
                   
        for i in range(1,len(arr)):
            ans += i * freq[arr[i]]
        print(arr)
        return ans