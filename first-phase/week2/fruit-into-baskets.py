class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}
        i, j, ans = 0, 0, 0
        
        while j < len(fruits):
            fruit_count[fruits[j]] = fruit_count.get(fruits[j], 0) + 1
            
            while len(fruit_count) > 2:
                if fruit_count[fruits[i]] == 1:
                    del fruit_count[fruits[i]]
                else:
                    fruit_count[fruits[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)
            j += 1
        
        return ans