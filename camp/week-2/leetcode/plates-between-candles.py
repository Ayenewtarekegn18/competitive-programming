class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        count = 0
        indx_candle = {}
        for i in range(len(s)):
            if s[i] == "|":
                indx_candle[i] = count
            else :
                count +=1
        candles = [ j for j in indx_candle]
        ans = []
        
        if len(indx_candle) == 0:
            return [0] * len(queries)
        
        for i in queries:
            l = bisect_left(candles,i[0])
            left = l if l < len(candles) else -1

            r = bisect_right(candles,i[1])-1
            right = r if r > 0 else 0

            plates = indx_candle[candles[right]] - indx_candle[candles[left]]

            if plates > 0:
                ans.append(plates)
            else:
                ans.append(0)
        return ans
                
