class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        n = len(processorTime) * 4
        processorTime.sort( reverse = True )
        ans = []
        for i in range(len(tasks)):
            if (i+1) % 4 == 0 :
                x = tasks[i] + processorTime[i//4]
                ans.append(x)
        # print(ans)
        return (max(ans))