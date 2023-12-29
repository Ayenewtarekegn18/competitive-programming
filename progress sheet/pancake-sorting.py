class Solution:
    def flip(self, arr: List[int], ind:int)->List[int]: 
        i = 0
        j = ind
        while (i < j ):
            arr[i], arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        return arr

    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        while n!=0:
            ind = arr.index(n)
            ans.append(ind+1)
            arr = self.flip(arr,ind)
            arr = self.flip(arr,n-1)
            ans.append(n)
            n -=1
        return ans