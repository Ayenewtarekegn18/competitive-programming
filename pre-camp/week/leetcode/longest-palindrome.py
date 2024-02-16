from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        odd = 0
        even = 0
        for i in s:
            freq[i] += 1
        
        for val in freq.values():
            if val % 2 == 0:
                even += val
            else:
                even += val - 1
                odd = 1
        
        ans = even + odd
        
        return ans