class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
      

      #bubble sort
        # for j in range(len(heights)):
        #     for k in range(len(heights)-j-1):
        #         if heights[k] < heights[k+1]:
        #             heights[k],heights[k+1] =  heights[k+1],heights[k]
        #             names[k],names[k+1] =  names[k+1],names[k]
        # return names
       
       #selection sort
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i] < heights[j]:
                    heights[i],heights[j] =  heights[j],heights[i]
                    names[i],names[j] =  names[j],names[i]
        return names
                    
            

    