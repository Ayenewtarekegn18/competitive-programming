class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # "cbacdcbcabshjebajjddd"
        
        ans = []
        freq = Counter(s)
        i = 0

        # print(freq)

        while i < len(s):
            
            if not ans:
                ans.append(s[i])
                freq[s[i]] -= 1
                i+=1
                
            elif s[i] in ans:
                # print("hey")
                freq[s[i]] -= 1
                i+=1
            

            elif ans[-1] > s[i] and freq[ans[-1]] > 0 : 
                # print("hey")
                ans.pop()

            else:
                ans.append(s[i])
                freq[s[i]] -= 1
                i+=1
            
            # print(ans)
        # print(freq)
        return "".join(ans)
