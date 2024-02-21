class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = []
        tens = []
        twenties = []
        for i in bills:
            # print(fives,tens,twenties)
            if i == 5:
                fives.append(i)
            elif i == 10 and len(fives) > 0:
                fives.pop()
                tens.append(i)
            elif i == 20 and len(fives) > 0:
                if len(tens) > 0:
                    fives.pop()
                    tens.pop()
                    twenties.append(i)

                elif len(tens) == 0 and len(fives) > 2:
                    x = 0
                    while x<3:
                        fives.pop()
                        x+=1 
                    twenties.append(i)
                else:
                    return False

            else:
                return False
        
        return True
            
                

            