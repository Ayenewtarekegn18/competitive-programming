class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ch = list(boxes)

        left = [0] * n
        count = int(ch[0])
        for i in range(1, n):
            left[i] = left[i - 1] + count
            count += int(ch[i])

        right = [0] * n
        count = int(ch[n - 1])
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + count
            count += int(ch[i])

        answer = [0] * n
        for i in range(n):
            answer[i] = left[i] + right[i]

        return answer


        