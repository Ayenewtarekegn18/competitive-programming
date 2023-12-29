class Solution:
    def comp(a: str, b: str) -> bool:
        return a + b > b + a
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        large = ""
        str_nums = []
        x = 0

        # Convert integers to strings and handle special case of all zeros
        for num in nums:
            if num == 0:
                x += 1
            str_nums.append(str(num))

        # Sort the strings in a custom order using the comp function
        str_nums.sort(key=lambda x: x * 10, reverse=True)

        # Concatenate sorted strings to form the largest number
        large = ''.join(str_nums)

        # Handle the case where all elements in nums are zero
        if x == n:
            return "0"
        else:
            return large

        # Example usage:
        sol = Solution()
        result = sol.largestNumber([3, 30, 34, 5, 9])
        print(result)