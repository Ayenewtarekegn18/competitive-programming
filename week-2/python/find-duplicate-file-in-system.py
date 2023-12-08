class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = {}
        ans = []
        for i in paths:
            n = i.split()
            direct = n[0] + "/"
            for x in n[1:]:
                index = x.index("(")
                file = x[index + 1: -1]
                if file in mp:
                    mp[file].append(direct + x[:index])
                else:
                    mp[file] = [direct + x[:index]]
        for key,val in mp.items():
            if len(val) > 1:
                ans.append(val)
        return ans
            

                      
        