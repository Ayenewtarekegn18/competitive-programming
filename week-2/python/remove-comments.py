class Solution:
    def removeComments(self, source: List[str]) -> List[str]: 
        flag = True
        ans = []
        s = ""
        for i in source:
            j = 0
            while j < len(i):
                if flag and i[j:j+2] == "//":
                    break
                elif flag and i[j:j+2] == "/*":
                    flag = False
                    j += 2
                    continue
                elif flag == False and i[j:j+2] == "*/":
                    flag = True
                    j += 2
                    continue
                elif flag == True:
                    s += i[j]
                j += 1 
            if len(s)>0 and flag:
                ans.append(s)
                s = ""
        return ans



