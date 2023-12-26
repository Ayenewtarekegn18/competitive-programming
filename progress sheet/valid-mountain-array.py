class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag = 0
        if len(arr)<3:
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1] or (flag == 0 and arr[i] > arr[i+1]):
                return False
            elif flag == 0 and arr[i] < arr[i+1]:
                flag = 1
            elif flag == 1  and arr[i] > arr[i+1]:
                flag = -1
            elif flag == -1 and arr[i] < arr[i+1]:
                return False
            
        return  flag == -1