class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> res(n, 0);
        vector<int> prefix(n, 0);
        
        for (auto booking : bookings) {
            prefix[booking[0]-1] += booking[2];
            if (booking[1]-1 < n-1) {
                prefix[booking[1]] -= booking[2];
            }
        }
        
        res[0]=prefix[0];
        for (int i=1; i<n; i++) {
            res[i] = res[i-1] + prefix[i];
        }
        
        return res;
    }
};
