class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def calc(l,r,turn):
            if turn:
                if l == r:
                    return nums[l]
                left = calc(l+1,r,not turn) + nums[l]
                right = calc(l,r-1,not turn) + nums[r]
                return max(left,right)
            else:
                if l == r:
                    return nums[l]
                left = calc(l+1,r,not turn) - nums[l]
                right = calc(l,r-1,not turn) - nums[r]
                return min(left,right)
        return calc(0,len(nums)-1,True) >=0
            
