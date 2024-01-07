class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maximum = 0
        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1

        maximum = max(current_count, maximum)

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1

            maximum = max(current_count, maximum)

        return maximum