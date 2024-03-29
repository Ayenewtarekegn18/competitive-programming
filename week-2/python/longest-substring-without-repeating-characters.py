class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_len = 0
        char_set = set()
  
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                char_set.remove(s[i])
                i += 1

        return max_len