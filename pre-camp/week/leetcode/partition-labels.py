class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        current = 0
        end = 0
        ans = []
        

        for i in range(len(s)):
            last[s[i]] = i
        print(last)
        while current < len(s):
            end = last[s[current]]
            j = current + 1
            while j < end:
                end = max(end,last[s[j]])
                j += 1
            ans.append(end - current+1)
            current = end + 1
        return ans
            
