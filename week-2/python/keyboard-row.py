class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word = ''
        row = []
        for i in words:
            flag1 = 0
            flag2 = 0
            flag3 = 0
            if i[0].lower() in  "qwertyuiop":
                flag1 =+ 1
            elif i[0].lower() in  "asdfghjkl":
                flag2 += 1
            elif i[0].lower() in  "zxcvbnm":
                flag3 += 1
            for j  in range(len(i)):
                if flag1==1:
                    if i[j].lower() in "qwertyuiop":
                        word += i[j]
                    else:
                        break
                elif flag2==1:
                    if i[j].lower() in "asdfghjkl":
                        word += i[j]
                    else:
                        break 
                elif flag3==1:
                    if i[j].lower() in "zxcvbnm":
                        word += i[j]
                    else: 
                        break
            else:
                row.append(word)
            word="" 
        return row
                    
                    