class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index =  defaultdict(int)
        for i in range(len(intervals)):
            index[intervals[i][0]] = i

        intervals.sort()
       # print(intervals)
        ans = [-1]*len(intervals)
        for i in intervals:
            l = 0
            r = len(intervals) - 1 
            check = [10**7,10**7]
            while l <= r:
                mid = (l+r)//2
                #print(intervals[mid])
                if i[1] <= intervals[mid][0]:
                    r = mid - 1 
                    check = min(check,intervals[mid])
                   
                else:
                    l = mid + 1
            #print(check)
            if check != [10**7,10**7]:
                ans[index[i[0]]] = index[check[0]]
            else:
                ans[index[i[0]]] = -1  
        return ans
