class Solution {
public:

int numOfSubarrays(vector<int>& a, int k, int threshold) {
        int count = 0, sum = 0;
        for(int i = 0; i < a.size(); i++) {
            sum += a[i];
            if(i >= k) sum -= a[i-k];
            if(i >= k-1 && sum /(k)>= threshold) count++;
        }
        return count;
    }
};
