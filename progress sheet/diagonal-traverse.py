class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        store = defaultdict(list)
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                store[i + j].append(mat[i][j])
        for k in store:
            if k % 2 == 0:
                ans += reversed(store[k])
            else:
                ans += store[k]

        return ans


        