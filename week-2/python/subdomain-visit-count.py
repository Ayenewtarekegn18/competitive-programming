class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}
        ans = []
        for domain in cpdomains:
            n,s = domain.split()
            n=int(n)
            for i in range(len(s)-1,-1,-1):
                if s[i] == ".":
                    subdomain = s[i+1:]
                    if subdomain in mp:
                        mp[subdomain] += n
                    else:
                        mp[subdomain] = n
            subdomain = s[i:]
            if subdomain in mp:
                mp[subdomain] += n
            else:
                mp[subdomain] = n
        for key,value in mp.items():
            ans.append(str(value) + " " + key)  
        return ans        