class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)  
        trainers.sort(reverse = True)  
        i = 0
        j = 0
        ans = 0
        while j <len(trainers) and i < len(players):
            if players[i] <= trainers[j]:
                i+=1
                j+=1
                ans+=1
            else:
                i += 1
        return ans
        
        

