class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [ 0 for _ in range(n+2)]
        for i in bookings:
            prefix[i[0]] += i[2]
            prefix[i[1]+1] -= i[2]
        total = 0
        for j in range(len(prefix)):
            total +=prefix[j]
            prefix[j] = total
        return prefix[1:-1]