class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        word = []
        maps = {2:"abc",
                3:"def",
                4:"ghi",
                5:"jkl",
                6:"mno",
                7:"pqrs",
                8:"tuv",
                9:"wxyz"
                }
        ans=[]
        path = []
        def backtrack(indx,path):
            if indx >= len(digits):
                ans.append("".join(path))
                return      
            for char in maps[int(digits[indx])]:
                path.append(char)
                backtrack(indx + 1,path)
                path.pop()
        backtrack(0,[])
        return ans
