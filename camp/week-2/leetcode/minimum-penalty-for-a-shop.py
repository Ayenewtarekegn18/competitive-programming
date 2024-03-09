class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_points = 0
        points = 0
        close_t = -1
        for i in range(len(customers)):
            if customers[i] == 'Y':
                points += 1
            else:
                points -= 1
            if points > max_points:
                max_points = points
                close_t = i
        return close_t + 1

     
        

