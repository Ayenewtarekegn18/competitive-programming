class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        indx = bisect_left(arr,x)
        l = indx - 1
        r = (indx) % len(arr)
        
        while k > 0:
            a = arr[l]
            b = arr[r]
            if abs(a-x) <= abs(b-x):
                k-=1
                ans.append(a)
                l-=1
            elif abs(a-x) > abs(b-x):
                k-=1
                ans.append(b)
                r = (r + 1) % len(arr)
                
        return sorted(ans)


