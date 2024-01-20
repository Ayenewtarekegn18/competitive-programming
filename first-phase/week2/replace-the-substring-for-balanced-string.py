class Solution:

    def balancedString(self, s: str) -> int:
        freq = defaultdict(int)
        excess = defaultdict(int)
        excess_check = defaultdict(int)
        count = float ("inf")
        amount = 0

        for i in s:
            freq[i] += 1

        for key,val in freq.items():
            if val> len(s)/4:
                excess[key] = val - len(s)//4
            
        l = 0
        print(excess)

        def helpme(exe: dict, e:dict)->bool:
            for key,val in e.items():
                if key not in exe or val > exe[key] : 
                    return False
            return True
        
        for i in range(len(s)):
            if s[i] in excess:
                excess_check[s[i]] +=1
            flag = helpme(excess_check,excess) 
            while flag and l <= i:
                count = min(count,i-l+1)
                if s[l] in excess_check:
                    excess_check[s[l]] -= 1
                l+=1
                flag = helpme(excess_check,excess) 
            print(excess_check)
                
        if count == float("inf") or len(excess) == 0:
            return 0 
        return count
            

            
            