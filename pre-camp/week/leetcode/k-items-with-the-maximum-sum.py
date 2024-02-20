class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        array = []
        array +=  [1] * numOnes
        array += [0] * numZeros
        array  += [-1]*numNegOnes
       
        return sum(array[:k])